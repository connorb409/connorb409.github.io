#!/usr/bin/env python3
"""
Charlotte County, FL Solar Permit Scraper - DEBUG VERSION
"""

import json
import logging
import re
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup

BASE_URL = "https://aca-prod.accela.com/BOCC/"
SEARCH_URL = urljoin(BASE_URL, "Cap/CapHome.aspx?module=Building&TabName=Building")

SOLAR_LICENSE_TYPES = [
    "C SOLAR ENERGY",
    "C SOLAR SYSTEM",
    "C SOLAR WAT HEAT",
]

LOOKBACK_DAYS = 365
OUTPUT_FILE = Path(__file__).parent / "permits.json"
CACHE_FILE = Path(__file__).parent / ".geocode_cache.json"
DEBUG_DIR = Path(__file__).parent / "debug_html"

REQUEST_DELAY_SEC = 1.5
PAGE_DELAY_SEC = 2.0

USER_AGENT = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/124.0.0.0 Safari/537.36"
)

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("solar-scraper")


def extract_form_state(html):
    soup = BeautifulSoup(html, "html.parser")
    state = {}
    for name in (
        "__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION",
        "__VIEWSTATEENCRYPTED", "__EVENTTARGET", "__EVENTARGUMENT",
    ):
        el = soup.find("input", {"name": name})
        if el is not None:
            state[name] = el.get("value", "")
    return state


def find_input_by_label_fragment(soup, label_fragment):
    for label in soup.find_all(string=re.compile(label_fragment, re.I)):
        parent = label.parent
        for _ in range(6):
            if parent is None:
                break
            ctrl = parent.find(["input", "select"])
            if ctrl is not None and ctrl.get("name"):
                return ctrl["name"]
            parent = parent.parent
    return None


def discover_field_names(html):
    soup = BeautifulSoup(html, "html.parser")
    fields = {}
    for select in soup.find_all("select"):
        opts = [o.get_text(strip=True) for o in select.find_all("option")]
        if any("SOLAR ENERGY" in o for o in opts):
            fields["license_type"] = select.get("name")
            log.info("DEBUG: found license_type select: %s", select.get("name"))
            break
    fields["start_date"] = find_input_by_label_fragment(soup, r"Start Date")
    fields["end_date"] = find_input_by_label_fragment(soup, r"End Date")
    log.info("DEBUG: discovered fields: %s", fields)
    for btn in soup.find_all("a"):
        if btn.get("title") == "Search" and "btnNewSearch" in (btn.get("href") or ""):
            m = re.search(r"WebForm_PostBackOptions\(new WebForm_PostBackOptions\(\"([^\"]+)\"", btn["href"])
            if m:
                fields["search_event_target"] = m.group(1)
                log.info("DEBUG: search button event target: %s", m.group(1))
                break
    return fields


def save_debug_html(html, label):
    DEBUG_DIR.mkdir(exist_ok=True)
    safe_label = re.sub(r"[^a-z0-9_]+", "_", label.lower())[:50]
    path = DEBUG_DIR / f"{safe_label}.html"
    path.write_text(html)
    log.info("DEBUG: saved %d chars to %s", len(html), path)


def run_search(session, license_type, start_date, end_date):
    log.info("=" * 60)
    log.info("Searching license type: %s (%s -> %s)", license_type, start_date, end_date)
    resp = session.get(SEARCH_URL, timeout=30)
    resp.raise_for_status()
    log.info("DEBUG: GET search page returned %d, length=%d", resp.status_code, len(resp.text))
    save_debug_html(resp.text, f"01_form_{license_type}")

    state = extract_form_state(resp.text)
    log.info("DEBUG: viewstate keys present: %s", list(state.keys()))
    fields = discover_field_names(resp.text)

    if not fields.get("license_type"):
        log.error("Could not locate License Type field. Site layout may have changed.")
        return []

    payload = {
        "__EVENTTARGET": fields.get("search_event_target", "ctl00$PlaceHolderMain$btnNewSearch"),
        "__EVENTARGUMENT": "",
        **state,
        fields["license_type"]: license_type,
    }
    if fields.get("start_date"):
        payload[fields["start_date"]] = start_date
    if fields.get("end_date"):
        payload[fields["end_date"]] = end_date

    log.info("DEBUG: POST payload keys: %s", list(payload.keys()))
    log.info("DEBUG: license_type field set to: %s", license_type)

    time.sleep(REQUEST_DELAY_SEC)
    resp = session.post(SEARCH_URL, data=payload, timeout=60)
    resp.raise_for_status()
    log.info("DEBUG: POST returned status=%d, length=%d, final URL=%s",
             resp.status_code, len(resp.text), resp.url)
    save_debug_html(resp.text, f"02_results_{license_type}")

    soup = BeautifulSoup(resp.text, "html.parser")
    log.info("DEBUG: results page title: %s", (soup.title.string.strip() if soup.title and soup.title.string else 'no title'))

    error_msgs = soup.select(".ACA_ErrorMessage, .ACA_Message_Error, [class*='error']")
    visible_errors = [e.get_text(strip=True)[:200] for e in error_msgs if e.get_text(strip=True)]
    if visible_errors:
        log.info("DEBUG: error/message elements: %s", visible_errors[:5])

    body_text = soup.get_text(" ", strip=True)
    log.info("DEBUG: first 800 chars of body: %s", body_text[:800])

    h_tags = [h.get_text(strip=True) for h in soup.select("h1, h2, h3") if h.get_text(strip=True)]
    log.info("DEBUG: headings on page: %s", h_tags[:10])

    permits = []
    page_num = 1
    while True:
        page_permits, has_next, next_target = parse_results_page(resp.text)
        log.info("  Page %d: parsed %d permits", page_num, len(page_permits))
        permits.extend(page_permits)
        if not has_next:
            break
        time.sleep(PAGE_DELAY_SEC)
        state = extract_form_state(resp.text)
        payload = {
            "__EVENTTARGET": next_target,
            "__EVENTARGUMENT": "",
            **state,
        }
        resp = session.post(SEARCH_URL, data=payload, timeout=60)
        resp.raise_for_status()
        page_num += 1
        if page_num > 50:
            break
    return permits


def parse_results_page(html):
    soup = BeautifulSoup(html, "html.parser")
    permits = []

    rows = soup.select("tr[id*='trDataRow']")
    log.info("DEBUG: rows via 'tr[id*=trDataRow]': %d", len(rows))

    if not rows:
        all_tables = soup.find_all("table")
        log.info("DEBUG: total tables on page: %d", len(all_tables))
        for i, table in enumerate(all_tables):
            headers = [th.get_text(strip=True).lower() for th in table.find_all("th")]
            if headers:
                log.info("DEBUG: table %d headers: %s", i, headers[:8])
            if any("record" in h for h in headers) and any("date" in h for h in headers):
                rows = table.find_all("tr")[1:]
                log.info("DEBUG: using table %d, found %d data rows", i, len(rows))
                break

    if not rows:
        gridviews = soup.select("[class*='GridView'], [id*='GridView'], [id*='gdvPermitList']")
        log.info("DEBUG: gridview-like elements found: %d", len(gridviews))
        for gv in gridviews[:3]:
            log.info("DEBUG: gridview id=%s, class=%s, rows inside=%d",
                     gv.get('id'), gv.get('class'), len(gv.find_all('tr')))

    for row in rows:
        cells = row.find_all("td")
        if len(cells) < 3:
            continue
        texts = [c.get_text(" ", strip=True) for c in cells]
        permit = {
            "raw_cells": texts,
            "date": _first_match(texts, r"^\d{1,2}/\d{1,2}/\d{2,4}$"),
            "record_number": _first_match(texts, r"^[A-Z0-9-]{5,}$"),
            "status": _last_status(texts),
            "address": _first_address(texts),
            "description": _longest_text(texts),
        }
        link = row.find("a", href=re.compile(r"CapDetail|Cap/.*Detail"))
        if link:
            permit["detail_url"] = urljoin(BASE_URL, link["href"])
            if not permit["record_number"]:
                permit["record_number"] = link.get_text(strip=True)
        if permit["record_number"]:
            permits.append(permit)

    has_next = False
    next_target = None
    for a in soup.find_all("a"):
        text = a.get_text(strip=True).lower()
        if text in ("next", ">", "next >"):
            href = a.get("href", "")
            m = re.search(r"__doPostBack\('([^']+)'", href)
            if m:
                has_next = True
                next_target = m.group(1)
                break
    return permits, has_next, next_target


def _first_match(texts, pattern):
    rx = re.compile(pattern)
    for t in texts:
        if rx.match(t):
            return t
    return None


def _longest_text(texts):
    return max(texts, key=len) if texts else ""


def _first_address(texts):
    for t in texts:
        if re.match(r"^\d+\s+\S+", t) and any(
            tok in t.upper()
            for tok in (" RD", " ST", " AVE", " BLVD", " DR", " LN", " CT",
                        " PKWY", " WAY", " TER", " CIR", " HWY", " TRL", " PL")
        ):
            return t
    return None


def _last_status(texts):
    status_keywords = (
        "issued", "review", "submitted", "pending", "approved", "void",​​​​​​​​​​​​​​​​
