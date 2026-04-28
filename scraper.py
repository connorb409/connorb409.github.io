#!/usr/bin/env python3
"""Charlotte County FL Solar Permit Scraper - debug version."""

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

SOLAR_LICENSE_TYPES = ["C SOLAR ENERGY", "C SOLAR SYSTEM", "C SOLAR WAT HEAT"]

LOOKBACK_DAYS = 365
OUTPUT_FILE = Path(__file__).parent / "permits.json"
CACHE_FILE = Path(__file__).parent / ".geocode_cache.json"
DEBUG_DIR = Path(__file__).parent / "debug_html"

REQUEST_DELAY_SEC = 1.5
PAGE_DELAY_SEC = 2.0

USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36"

logging.basicConfig(level=logging.INFO, format="%(asctime)s [%(levelname)s] %(message)s")
log = logging.getLogger("scraper")


def extract_form_state(html):
    soup = BeautifulSoup(html, "html.parser")
    state = {}
    names = ["__VIEWSTATE", "__VIEWSTATEGENERATOR", "__EVENTVALIDATION", "__VIEWSTATEENCRYPTED", "__EVENTT​​​​​​​​​​​​​​​​
