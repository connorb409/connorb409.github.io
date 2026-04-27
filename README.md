<!DOCTYPE html>

<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Florida Solar Permits Scanner</title>
<style>
:root {
  --bg: #0a0e15;
  --panel: #121824;
  --card: #1a2234;
  --card2: #222b40;
  --border: #242e43;
  --border2: #2d3854;
  --text: #e8edf5;
  --muted: #7c8ba5;
  --dim: #4a5670;
  --sun: #FFB800;
  --sun2: #FF7A00;
  --pending: #F59E0B;
  --review: #3B82F6;
  --issued: #10B981;
  --final: #6B7280;
  --hold: #EF4444;
}

- { box-sizing: border-box; margin: 0; padding: 0; }
  html, body { height: 100%; overflow: hidden; font-family: system-ui, -apple-system, “Segoe UI”, Roboto, sans-serif; }
  body { background: var(–bg); color: var(–text); display: flex; flex-direction: column; }

/* ── TOP BAR ── */
.topbar {
background: var(–panel);
border-bottom: 1px solid var(–border);
height: 60px;
padding: 0 18px;
display: flex;
align-items: center;
gap: 16px;
z-index: 1000;
flex-shrink: 0;
}

.logo { display: flex; align-items: center; gap: 10px; font-size: 19px; font-weight: 800; flex-shrink: 0; }
.logo-icon {
width: 30px; height: 30px;
background: radial-gradient(circle, #FFE066 0%, #FFB800 60%, #FF7A00 100%);
border-radius: 50%;
box-shadow: 0 0 14px rgba(255,184,0,0.5);
animation: logo-pulse 3s ease-in-out infinite;
}
@keyframes logo-pulse {
0%,100% { box-shadow: 0 0 14px rgba(255,184,0,0.5); }
50% { box-shadow: 0 0 28px rgba(255,184,0,0.9); }
}
.logo span { color: var(–sun); }
.byline {
font-size: 9px; font-weight: 500; color: var(–muted);
letter-spacing: 0.8px; margin-left: 4px; text-transform: lowercase;
font-style: italic; align-self: flex-end; padding-bottom: 4px;
}

/* ── CITY PICKER ── */
.city-picker {
position: relative;
margin-left: 8px;
}

.city-btn {
background: var(–card);
border: 1px solid var(–border);
color: var(–text);
padding: 8px 14px 8px 12px;
border-radius: 4px;
font-family: inherit;
font-size: 13px;
font-weight: 600;
cursor: pointer;
display: flex;
align-items: center;
gap: 8px;
min-width: 200px;
transition: all 0.12s;
}
.city-btn:hover { border-color: var(–sun); }
.city-btn.open { border-color: var(–sun); background: var(–card2); }
.city-btn .city-meta { color: var(–muted); font-size: 11px; font-weight: 500; }
.city-btn .chevron { margin-left: auto; color: var(–muted); transition: transform 0.2s; }
.city-btn.open .chevron { transform: rotate(180deg); }

.city-dropdown {
position: absolute;
top: calc(100% + 4px);
left: 0;
background: var(–panel);
border: 1px solid var(–border2);
border-radius: 4px;
min-width: 280px;
max-height: 60vh;
overflow-y: auto;
box-shadow: 0 10px 40px rgba(0,0,0,0.6);
z-index: 2000;
display: none;
padding: 4px;
}
.city-dropdown.open { display: block; }

.city-search {
width: 100%;
background: var(–card);
border: 1px solid var(–border);
color: var(–text);
padding: 8px 12px;
font-size: 13px;
border-radius: 3px;
outline: none;
font-family: inherit;
margin-bottom: 4px;
}
.city-search:focus { border-color: var(–sun); }

.city-group-label {
font-size: 9px; letter-spacing: 1.5px; color: var(–dim);
text-transform: uppercase; padding: 8px 12px 4px; font-weight: 700;
}

.city-option {
padding: 8px 12px;
cursor: pointer;
border-radius: 3px;
display: flex;
justify-content: space-between;
align-items: center;
gap: 12px;
font-size: 13px;
transition: background 0.1s;
}
.city-option:hover { background: var(–card); }
.city-option.active { background: rgba(255,184,0,0.1); border: 1px solid rgba(255,184,0,0.3); }
.city-option-name { font-weight: 600; }
.city-option-meta { color: var(–muted); font-size: 11px; }
.city-option .badge {
background: rgba(255,184,0,0.12);
color: var(–sun);
font-size: 9px;
letter-spacing: 0.5px;
padding: 2px 6px;
border-radius: 2px;
font-weight: 700;
text-transform: uppercase;
}
.city-option .badge.live { background: rgba(16,185,129,0.12); color: var(–issued); }
.city-option .badge.beta { background: rgba(59,130,246,0.12); color: var(–review); }

/* ── VIEW TOGGLE ── */
.view-toggle {
display: flex;
background: var(–card);
border: 1px solid var(–border);
border-radius: 4px;
padding: 2px;
margin-left: auto;
}

.view-btn {
background: transparent;
border: none;
color: var(–muted);
font-family: inherit;
font-size: 11px;
font-weight: 700;
letter-spacing: 1px;
text-transform: uppercase;
padding: 6px 12px;
cursor: pointer;
border-radius: 3px;
transition: all 0.12s;
}
.view-btn.on { background: var(–sun); color: #000; }
.view-btn:not(.on):hover { color: var(–text); }

/* ── REFRESH BUTTON ── */
.refresh-btn {
background: var(–card);
border: 1px solid var(–border);
color: var(–text);
font-family: inherit;
font-size: 11px;
font-weight: 700;
letter-spacing: 1px;
padding: 8px 12px;
cursor: pointer;
border-radius: 4px;
text-transform: uppercase;
display: flex;
align-items: center;
gap: 6px;
transition: all 0.12s;
}
.refresh-btn:hover { border-color: var(–sun); color: var(–sun); }
.refresh-btn:disabled { opacity: 0.5; cursor: not-allowed; }
.refresh-btn .spin { display: inline-block; transition: transform 0.5s; }
.refresh-btn.refreshing .spin { animation: spin 0.9s linear infinite; }
@keyframes spin { to { transform: rotate(360deg); } }

/* ── PRO BADGE ── */
.pro-btn {
background: linear-gradient(135deg, var(–sun), var(–sun2));
border: none;
color: #000;
font-family: inherit;
font-size: 11px;
font-weight: 800;
letter-spacing: 1px;
padding: 8px 14px;
cursor: pointer;
border-radius: 4px;
text-transform: uppercase;
}
.pro-btn:hover { filter: brightness(1.1); }

/* ── APP BODY ── */
.app-body { display: flex; flex: 1; overflow: hidden; min-height: 0; }

.sidebar {
width: 320px;
background: var(–panel);
border-right: 1px solid var(–border);
display: flex;
flex-direction: column;
overflow: hidden;
flex-shrink: 0;
}
.sidebar-header { padding: 14px 16px; border-bottom: 1px solid var(–border); }
.sidebar-title {
font-size: 9px; letter-spacing: 1.5px; color: var(–muted);
text-transform: uppercase; margin-bottom: 8px; font-weight: 600;
}

.filter-row { display: flex; gap: 6px; flex-wrap: wrap; }

.chip {
background: var(–card); border: 1px solid var(–border); color: var(–muted);
font-size: 10px; padding: 5px 10px; border-radius: 3px; cursor: pointer;
letter-spacing: 0.5px; transition: all 0.12s; text-transform: uppercase;
font-weight: 700; user-select: none;
}
.chip:hover { border-color: var(–sun); color: var(–sun); }
.chip.on { background: rgba(255,184,0,0.12); border-color: var(–sun); color: var(–sun); }
.chip[data-status=Pending].on { background: rgba(245,158,11,0.18); border-color: var(–pending); color: var(–pending); }
.chip[data-status=“In Review”].on { background: rgba(59,130,246,0.18); border-color: var(–review); color: var(–review); }
.chip[data-status=Issued].on { background: rgba(16,185,129,0.18); border-color: var(–issued); color: var(–issued); }
.chip[data-status=Final].on { background: rgba(107,114,128,0.22); border-color: var(–final); color: var(–text); }
.chip[data-status=“On Hold”].on { background: rgba(239,68,68,0.18); border-color: var(–hold); color: var(–hold); }

.search-input, .filter-input {
width: 100%; background: var(–card); border: 1px solid var(–border);
color: var(–text); font-size: 12px; padding: 7px 10px; border-radius: 3px;
outline: none; font-family: inherit;
}
.search-input:focus, .filter-input:focus { border-color: var(–sun); }
.search-input::placeholder, .filter-input::placeholder { color: var(–muted); }

.date-range {
display: flex; gap: 6px; align-items: center;
}
.date-range .filter-input { font-size: 11px; padding: 6px 8px; }
.date-range .sep { color: var(–muted); font-size: 10px; }

.permit-list { flex: 1; overflow-y: auto; padding: 8px; }
.permit-list::-webkit-scrollbar { width: 4px; }
.permit-list::-webkit-scrollbar-thumb { background: var(–border); border-radius: 2px; }

.permit-card {
background: var(–card); border: 1px solid var(–border); border-radius: 4px;
padding: 9px 11px; margin-bottom: 5px; cursor: pointer; transition: all 0.15s;
position: relative;
}
.permit-card::before {
content: ‘’; position: absolute; left: 0; top: 0; bottom: 0;
width: 3px; border-radius: 4px 0 0 4px;
}
.permit-card[data-status=Pending]::before { background: var(–pending); }
.permit-card[data-status=“In Review”]::before { background: var(–review); }
.permit-card[data-status=Issued]::before { background: var(–issued); }
.permit-card[data-status=Final]::before { background: var(–final); }
.permit-card[data-status=“On Hold”]::before { background: var(–hold); }
.permit-card:hover { background: rgba(255,184,0,0.05); transform: translateX(2px); }
.permit-card.selected { border-color: var(–sun); background: rgba(255,184,0,0.08); }

.permit-addr { font-size: 12px; font-weight: 700; margin-bottom: 2px; line-height: 1.3; }
.permit-meta { font-size: 10px; color: var(–muted); letter-spacing: 0.3px; font-weight: 500; }
.permit-meta strong { color: var(–text); font-weight: 700; }

/* ── MAIN CONTENT ── */
.main-content {
flex: 1; position: relative; background: #0d1220; overflow: hidden;
}

/* MAP */
#map-container {
width: 100%; height: 100%; position: relative;
cursor: grab; display: none;
}
#map-container.active { display: block; }
#map-container:active { cursor: grabbing; }

#tile-layer { position: absolute; inset: 0; }

.map-tile {
position: absolute;
user-select: none;
pointer-events: none;
filter: invert(0.92) hue-rotate(180deg) brightness(0.92) saturate(0.6);
transition: opacity 0.2s;
}

#pin-layer { position: absolute; inset: 0; pointer-events: none; }

.map-pin {
position: absolute;
transform: translate(-50%, -100%);
pointer-events: auto;
cursor: pointer;
transition: transform 0.15s;
z-index: 10;
}
.map-pin:hover { transform: translate(-50%, -100%) scale(1.15); z-index: 20; }
.map-pin.selected { z-index: 30; transform: translate(-50%, -100%) scale(1.25); }

.pin-marker {
width: 24px; height: 24px;
border-radius: 50% 50% 50% 0;
transform: rotate(-45deg);
border: 2px solid rgba(0,0,0,0.5);
display: flex; align-items: center; justify-content: center;
}
.pin-marker.urgent {
width: 28px; height: 28px;
animation: pin-pulse 2s ease-in-out infinite;
}
.pin-icon {
transform: rotate(45deg);
color: #000; font-weight: 900; font-size: 12px; line-height: 1;
font-family: monospace;
}
.pin-marker.urgent .pin-icon { font-size: 14px; }
@keyframes pin-pulse {
0%,100% { box-shadow: 0 0 6px rgba(245,158,11,0.6); }
50% { box-shadow: 0 0 18px rgba(245,158,11,1), 0 0 32px rgba(245,158,11,0.4); }
}

.popup {
position: absolute;
transform: translate(-50%, calc(-100% - 36px));
background: var(–panel); border: 1px solid var(–border);
border-radius: 4px; padding: 12px 14px;
min-width: 240px; max-width: 280px;
box-shadow: 0 8px 24px rgba(0,0,0,0.6);
pointer-events: auto; z-index: 100;
}
.popup::after {
content: ‘’; position: absolute; bottom: -8px; left: 50%; transform: translateX(-50%);
width: 0; height: 0;
border-left: 8px solid transparent; border-right: 8px solid transparent;
border-top: 8px solid var(–panel);
}
.popup-close {
position: absolute; top: 6px; right: 8px;
background: none; border: none; color: var(–muted);
font-size: 16px; cursor: pointer; padding: 2px 6px; line-height: 1;
}
.popup-close:hover { color: var(–text); }
.popup-title { font-size: 14px; font-weight: 800; margin-bottom: 6px; padding-right: 16px; line-height: 1.3; }
.popup-status {
display: inline-block; font-size: 9px; font-weight: 700;
padding: 2px 8px; border-radius: 2px; letter-spacing: 1px;
margin-bottom: 8px; text-transform: uppercase;
}
.popup-status[data-status=Pending] { background: rgba(245,158,11,0.2); color: var(–pending); }
.popup-status[data-status=“In Review”] { background: rgba(59,130,246,0.2); color: var(–review); }
.popup-status[data-status=Issued] { background: rgba(16,185,129,0.2); color: var(–issued); }
.popup-status[data-status=Final] { background: rgba(107,114,128,0.25); color: #cbd5e1; }
.popup-status[data-status=“On Hold”] { background: rgba(239,68,68,0.2); color: var(–hold); }
.popup-meta { font-size: 11px; color: var(–muted); line-height: 1.6; }
.popup-meta strong { color: var(–text); font-weight: 600; }

/* MAP CONTROLS */
.map-controls {
position: absolute; top: 12px; right: 12px;
display: flex; flex-direction: column; gap: 4px; z-index: 50;
}
.map-btn {
width: 32px; height: 32px;
background: rgba(18,24,36,0.94); border: 1px solid var(–border); color: var(–text);
font-size: 18px; cursor: pointer; border-radius: 3px;
display: flex; align-items: center; justify-content: center;
transition: all 0.12s; line-height: 1; font-family: inherit;
backdrop-filter: blur(8px);
}
.map-btn:hover { border-color: var(–sun); color: var(–sun); }

.map-info {
position: absolute; bottom: 12px; left: 12px;
background: rgba(18,24,36,0.85); border: 1px solid var(–border); border-radius: 3px;
padding: 6px 10px; font-size: 10px; color: var(–muted); z-index: 50;
pointer-events: none; letter-spacing: 0.3px;
}
.attribution {
position: absolute; bottom: 4px; right: 4px;
background: rgba(18,24,36,0.7); border-radius: 2px;
padding: 2px 6px; font-size: 9px; color: var(–muted); z-index: 49;
}
.attribution a { color: var(–sun); text-decoration: none; }
.map-legend {
position: absolute; bottom: 30px; right: 12px;
background: rgba(18,24,36,0.94); border: 1px solid var(–border);
border-radius: 4px; padding: 10px 12px; z-index: 50;
backdrop-filter: blur(8px);
}
.legend-title {
font-size: 9px; letter-spacing: 1.5px; color: var(–muted);
text-transform: uppercase; margin-bottom: 6px; font-weight: 700;
}
.legend-row {
display: flex; align-items: center; gap: 8px; margin-bottom: 3px;
font-size: 11px; font-weight: 500;
}
.legend-dot {
width: 10px; height: 10px; border-radius: 50%;
border: 1.5px solid rgba(0,0,0,0.4); flex-shrink: 0;
}

/* TABLE VIEW */
#table-container {
width: 100%; height: 100%; display: none;
background: var(–bg); overflow: auto;
}
#table-container.active { display: block; }

.table-toolbar {
position: sticky; top: 0; z-index: 10;
padding: 14px 18px;
background: var(–panel);
border-bottom: 1px solid var(–border);
display: flex;
gap: 12px;
flex-wrap: wrap;
align-items: center;
}

.toolbar-stat {
font-size: 11px; color: var(–muted); display: flex; align-items: center; gap: 6px;
}
.toolbar-stat strong { color: var(–text); font-size: 14px; font-weight: 700; }
.toolbar-stat .stat-dot { width: 8px; height: 8px; border-radius: 50%; }

.permits-table {
width: 100%;
border-collapse: separate;
border-spacing: 0;
font-size: 13px;
}

.permits-table thead th {
position: sticky;
top: 53px;
background: var(–panel);
color: var(–muted);
font-size: 10px;
letter-spacing: 1.2px;
text-transform: uppercase;
font-weight: 700;
text-align: left;
padding: 10px 14px;
border-bottom: 1px solid var(–border);
cursor: pointer;
user-select: none;
white-space: nowrap;
}
.permits-table thead th:hover { color: var(–sun); }
.permits-table thead th .sort-arrow { color: var(–sun); margin-left: 4px; font-size: 9px; }

.permits-table tbody tr {
border-bottom: 1px solid var(–border);
cursor: pointer;
transition: background 0.1s;
}
.permits-table tbody tr:hover { background: var(–card); }
.permits-table tbody tr.selected { background: rgba(255,184,0,0.08); }

.permits-table td {
padding: 11px 14px;
vertical-align: middle;
}
.cell-permit { font-family: ‘JetBrains Mono’, ‘SF Mono’, Consolas, monospace; font-size: 12px; color: var(–muted); }
.cell-address { font-weight: 600; }
.cell-address .city-tag { color: var(–muted); font-weight: 500; font-size: 11px; }
.cell-contractor { color: var(–muted); }
.cell-date { font-family: ‘JetBrains Mono’, ‘SF Mono’, Consolas, monospace; font-size: 12px; color: var(–muted); }

.status-pill {
display: inline-block;
font-size: 9px;
font-weight: 700;
padding: 3px 8px;
border-radius: 3px;
letter-spacing: 1px;
text-transform: uppercase;
}
.status-pill[data-status=Pending] { background: rgba(245,158,11,0.18); color: var(–pending); }
.status-pill[data-status=“In Review”] { background: rgba(59,130,246,0.18); color: var(–review); }
.status-pill[data-status=Issued] { background: rgba(16,185,129,0.18); color: var(–issued); }
.status-pill[data-status=Final] { background: rgba(107,114,128,0.22); color: #cbd5e1; }
.status-pill[data-status=“On Hold”] { background: rgba(239,68,68,0.18); color: var(–hold); }

/* LOADING / EMPTY / ERROR */
.state-overlay {
position: absolute; inset: 0;
display: none;
flex-direction: column;
align-items: center;
justify-content: center;
background: var(–bg);
z-index: 200;
text-align: center;
padding: 40px;
}
.state-overlay.show { display: flex; }

.state-icon {
font-size: 40px; margin-bottom: 16px; opacity: 0.5;
}

.loading-sun {
width: 50px; height: 50px;
background: radial-gradient(circle, #FFE066 0%, #FFB800 60%, #FF7A00 100%);
border-radius: 50%;
animation: load-pulse 1.2s ease-in-out infinite;
margin-bottom: 18px;
}
@keyframes load-pulse {
0%,100% { transform: scale(1); box-shadow: 0 0 20px rgba(255,184,0,0.4); }
50% { transform: scale(1.1); box-shadow: 0 0 40px rgba(255,184,0,0.7); }
}

.state-title {
font-size: 16px; font-weight: 700; color: var(–sun); letter-spacing: 1.5px;
text-transform: uppercase; margin-bottom: 6px;
}
.state-subtitle {
font-size: 12px; color: var(–muted); max-width: 420px;
line-height: 1.6;
}

.state-overlay.error .state-icon { color: var(–hold); }
.state-overlay.error .state-title { color: var(–hold); }

.state-overlay.empty .state-icon { color: var(–muted); }
.state-overlay.empty .state-title { color: var(–muted); }

/* PAYWALL MODAL */
.modal-overlay {
position: fixed; inset: 0;
background: rgba(0,0,0,0.75);
display: none;
align-items: center;
justify-content: center;
z-index: 5000;
padding: 20px;
backdrop-filter: blur(4px);
}
.modal-overlay.show { display: flex; }

.modal {
background: var(–panel);
border: 1px solid var(–border2);
border-radius: 8px;
padding: 32px;
max-width: 460px;
width: 100%;
position: relative;
box-shadow: 0 20px 60px rgba(0,0,0,0.8);
}

.modal-close {
position: absolute; top: 14px; right: 14px;
background: none; border: none; color: var(–muted);
font-size: 22px; cursor: pointer; line-height: 1;
}
.modal-close:hover { color: var(–text); }

.modal-icon {
font-size: 38px;
margin-bottom: 14px;
text-align: center;
}

.modal h2 {
font-size: 22px; font-weight: 800; margin-bottom: 8px; text-align: center;
background: linear-gradient(135deg, var(–sun), var(–sun2));
-webkit-background-clip: text; -webkit-text-fill-color: transparent;
background-clip: text;
}

.modal-sub { color: var(–muted); font-size: 13px; line-height: 1.6; margin-bottom: 24px; text-align: center; }

.feature-list { list-style: none; padding: 0; margin-bottom: 24px; }
.feature-list li {
padding: 8px 0;
font-size: 13px;
display: flex;
align-items: center;
gap: 10px;
}
.feature-list li::before {
content: ‘✓’;
color: var(–issued);
font-weight: 900;
font-size: 14px;
flex-shrink: 0;
}

.modal-cta {
width: 100%;
background: linear-gradient(135deg, var(–sun), var(–sun2));
border: none;
color: #000;
font-family: inherit;
font-size: 14px;
font-weight: 800;
letter-spacing: 1.5px;
padding: 12px;
border-radius: 4px;
cursor: pointer;
text-transform: uppercase;
}
.modal-cta:hover { filter: brightness(1.1); }

.modal-note {
text-align: center;
font-size: 11px;
color: var(–muted);
margin-top: 14px;
}

/* TOAST */
.toast {
position: fixed;
bottom: 24px;
left: 50%;
transform: translateX(-50%) translateY(20px);
background: var(–card);
border: 1px solid var(–border);
color: var(–text);
font-size: 12px;
font-weight: 600;
padding: 10px 18px;
border-radius: 4px;
opacity: 0;
transition: all 0.3s;
z-index: 9999;
pointer-events: none;
}
.toast.show { opacity: 1; transform: translateX(-50%) translateY(0); }
.toast.success { border-color: var(–issued); color: var(–issued); }
.toast.error { border-color: var(–hold); color: var(–hold); }

@media (max-width: 880px) {
.city-btn { min-width: 160px; }
.city-btn .city-meta { display: none; }
.byline { display: none; }
.pro-btn span.label { display: none; }
}
@media (max-width: 720px) {
.sidebar { width: 240px; }
.topbar { gap: 8px; padding: 0 12px; }
.refresh-btn span:not(.spin) { display: none; }
}
@media (max-width: 540px) {
.sidebar { display: none; }
.city-btn { min-width: 130px; font-size: 12px; padding: 7px 10px; }
}
</style>

</head>
<body>

<!-- ── TOP BAR ── -->

<div class="topbar">
  <div class="logo">
    <div class="logo-icon"></div>
    <div>FLORIDA<span>SOLAR</span></div>
    <div class="byline">created by connor</div>
  </div>

  <!-- City picker dropdown -->

  <div class="city-picker">
    <button class="city-btn" id="city-btn" onclick="toggleCityDropdown(event)">
      <span id="city-btn-label">Select City…</span>
      <span class="city-meta" id="city-btn-meta"></span>
      <span class="chevron">▾</span>
    </button>
    <div class="city-dropdown" id="city-dropdown">
      <input class="city-search" id="city-search" placeholder="Search cities…" oninput="filterCityList()" onclick="event.stopPropagation()">
      <div id="city-list"></div>
    </div>
  </div>

  <button class="refresh-btn" id="refresh-btn" onclick="refreshData()" title="Refresh permit data">
    <span class="spin">↻</span>
    <span>Refresh</span>
  </button>

  <div class="view-toggle">
    <button class="view-btn on" data-view="map" onclick="setView('map')">Map</button>
    <button class="view-btn" data-view="table" onclick="setView('table')">Table</button>
  </div>

  <button class="pro-btn" onclick="showPaywall('all-cities')">
    ⭐ <span class="label">Upgrade</span>
  </button>
</div>

<!-- ── BODY ── -->

<div class="app-body">
  <div class="sidebar">
    <div class="sidebar-header">
      <div class="sidebar-title">Status</div>
      <div class="filter-row" id="status-filters">
        <div class="chip on" data-status="all" onclick="setStatusFilter(this)">ALL</div>
        <div class="chip" data-status="Pending" onclick="setStatusFilter(this)">PENDING</div>
        <div class="chip" data-status="In Review" onclick="setStatusFilter(this)">IN REVIEW</div>
        <div class="chip" data-status="Issued" onclick="setStatusFilter(this)">ISSUED</div>
        <div class="chip" data-status="Final" onclick="setStatusFilter(this)">FINAL</div>
        <div class="chip" data-status="On Hold" onclick="setStatusFilter(this)">ON HOLD</div>
      </div>

```
  <div class="sidebar-title" style="margin-top:14px">Date Applied</div>
  <div class="date-range">
    <input class="filter-input" type="date" id="date-from" oninput="render()" />
    <span class="sep">to</span>
    <input class="filter-input" type="date" id="date-to" oninput="render()" />
  </div>

  <div class="sidebar-title" style="margin-top:14px">Contractor</div>
  <input class="search-input" id="contractor-filter" placeholder="Filter by contractor…" oninput="render()" />

  <div class="sidebar-title" style="margin-top:14px">Search</div>
  <input class="search-input" id="search" placeholder="Address, permit #, description…" />
</div>
<div class="permit-list" id="permit-list"></div>
```

  </div>

  <div class="main-content">
    <!-- MAP VIEW -->
    <div id="map-container" class="active">
      <div id="tile-layer"></div>
      <div id="pin-layer"></div>
      <div class="map-controls">
        <button class="map-btn" onclick="zoomIn()" title="Zoom in">+</button>
        <button class="map-btn" onclick="zoomOut()" title="Zoom out" style="font-size:22px">−</button>
        <button class="map-btn" onclick="fitAll()" title="Fit all" style="font-size:14px">⊡</button>
      </div>
      <div class="map-info">Drag · Scroll to zoom</div>
      <div class="map-legend">
        <div class="legend-title">Status</div>
        <div class="legend-row"><div class="legend-dot" style="background:#F59E0B"></div> Pending</div>
        <div class="legend-row"><div class="legend-dot" style="background:#3B82F6"></div> In Review</div>
        <div class="legend-row"><div class="legend-dot" style="background:#10B981"></div> Issued</div>
        <div class="legend-row"><div class="legend-dot" style="background:#6B7280"></div> Final</div>
        <div class="legend-row"><div class="legend-dot" style="background:#EF4444"></div> On Hold</div>
      </div>
      <div class="attribution">© <a href="https://www.openstreetmap.org/copyright" target="_blank" rel="noopener">OpenStreetMap</a></div>
    </div>

```
<!-- TABLE VIEW -->
<div id="table-container">
  <div class="table-toolbar" id="table-toolbar"></div>
  <table class="permits-table" id="permits-table">
    <thead>
      <tr>
        <th data-sort="id">Permit # <span class="sort-arrow"></span></th>
        <th data-sort="address">Address <span class="sort-arrow"></span></th>
        <th data-sort="contractor">Contractor <span class="sort-arrow"></span></th>
        <th data-sort="applied">Issue Date <span class="sort-arrow"></span></th>
        <th data-sort="status">Status <span class="sort-arrow"></span></th>
      </tr>
    </thead>
    <tbody id="table-body"></tbody>
  </table>
</div>

<!-- STATE OVERLAYS -->
<div class="state-overlay" id="state-loading">
  <div class="loading-sun"></div>
  <div class="state-title">Loading Permits</div>
  <div class="state-subtitle" id="loading-sub">Fetching data…</div>
</div>

<div class="state-overlay empty" id="state-empty">
  <div class="state-icon">📋</div>
  <div class="state-title">No Data</div>
  <div class="state-subtitle" id="empty-sub">No permits available for this city yet.</div>
</div>

<div class="state-overlay error" id="state-error">
  <div class="state-icon">⚠</div>
  <div class="state-title">Failed to Load</div>
  <div class="state-subtitle" id="error-sub">Couldn't fetch permit data. Please try again.</div>
  <button class="refresh-btn" style="margin-top:18px" onclick="refreshData()">↻ Retry</button>
</div>

<div class="state-overlay" id="state-welcome">
  <div class="state-icon">🌴</div>
  <div class="state-title" style="color:var(--text)">Welcome</div>
  <div class="state-subtitle">Select a Florida city above to start scanning solar permits.</div>
</div>
```

  </div>
</div>

<!-- ── PAYWALL MODAL ── -->

<div class="modal-overlay" id="paywall">
  <div class="modal">
    <button class="modal-close" onclick="hidePaywall()">×</button>
    <div class="modal-icon">⭐</div>
    <h2 id="paywall-title">FloridaSolar Pro</h2>
    <div class="modal-sub" id="paywall-sub">Unlock the full Florida network and live data feeds.</div>
    <ul class="feature-list" id="paywall-features">
      <li>All <strong>411 Florida cities</strong> &amp; counties</li>
      <li><strong>Live data feeds</strong> — refreshed daily</li>
      <li>Property owner contact info &amp; phone numbers</li>
      <li>Export to CSV / Excel / Google Sheets</li>
      <li>Webhook alerts for new pending permits</li>
      <li>API access for integrations</li>
    </ul>
    <button class="modal-cta" onclick="handleUpgrade()">Start 7-Day Free Trial</button>
    <div class="modal-note">$49 / mo after trial · Cancel anytime</div>
  </div>
</div>

<!-- TOAST -->

<div class="toast" id="toast"></div>

<script>
// ════════════════════════════════════════════════════════════════════
// EMBEDDED SAMPLE DATA
// ────────────────────────────────────────────────────────────────────
// In production, replace these embedded blobs with HTTP fetches from
// permits-{cityId}.json files (see StaticJsonAdapter below).
// ════════════════════════════════════════════════════════════════════
const EMBEDDED_DATA = {"miami":[{"id":"BP-3E82D8A8","address":"21377 Biscayne Blvd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.735856,"lng":-80.240053,"contractor":"Goldin Solar","applied":"2026-03-20","description":"8.9kW roof-mount solar PV, 22 panels"},{"id":"BP-2FF50512","address":"13643 NW 36th St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Final","lat":25.810749,"lng":-80.210306,"contractor":"Solar Energy Management","applied":"2025-12-28","description":"4.6kW roof-mount solar PV, 11 panels"},{"id":"BP-A8AB1E16","address":"418 Bird Rd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.78194,"lng":-80.185261,"contractor":"Goldin Solar","applied":"2026-04-16","description":"13.9kW roof-mount solar PV, 34 panels"},{"id":"BP-13C157EB","address":"25033 Coconut Grove Dr, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.773093,"lng":-80.154043,"contractor":"Cutting Edge Solar","applied":"2026-04-16","description":"9.4kW roof-mount solar PV, 23 panels"},{"id":"BP-B44D0E32","address":"1513 Flagler St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.798583,"lng":-80.18538,"contractor":"Brilliant Harvest Solar","applied":"2026-04-19","description":"5.5kW roof-mount solar PV, 13 panels"},{"id":"BP-8831B6DE","address":"12446 SW 8th St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.756036,"lng":-80.189403,"contractor":"A1A Solar Contracting","applied":"2026-01-22","description":"10.4kW roof-mount solar PV, 26 panels"},{"id":"BP-5CAB4186","address":"9236 Calle Ocho, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.744216,"lng":-80.189291,"contractor":"Cutting Edge Solar","applied":"2026-02-11","description":"6.2kW roof-mount solar PV, 15 panels"},{"id":"BP-085CDBB5","address":"15015 NW 36th St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.710615,"lng":-80.156617,"contractor":"Florida Power Services","applied":"2026-03-29","description":"10.3kW roof-mount solar PV, 25 panels"},{"id":"BP-D09A9BD8","address":"18820 Coconut Grove Dr, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Final","lat":25.779817,"lng":-80.134607,"contractor":"Brilliant Harvest Solar","applied":"2026-01-24","description":"13.2kW roof-mount solar PV, 33 panels"},{"id":"BP-9248BFB6","address":"19791 NE 2nd Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.804422,"lng":-80.132941,"contractor":"Solar Sky Group","applied":"2026-03-22","description":"5.1kW roof-mount solar PV, 12 panels"},{"id":"BP-A3910096","address":"4592 NW 36th St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.771175,"lng":-80.216398,"contractor":"EcoView Solar","applied":"2026-01-26","description":"9.7kW roof-mount solar PV, 24 panels"},{"id":"BP-BB4B41A0","address":"29287 Coconut Grove Dr, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.810532,"lng":-80.229295,"contractor":"Cutting Edge Solar","applied":"2026-03-19","description":"9.0kW roof-mount solar PV, 22 panels"},{"id":"BP-9A6A600F","address":"4794 NW 36th St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.703808,"lng":-80.219162,"contractor":"Sunshine State Solar","applied":"2026-03-11","description":"13.2kW roof-mount solar PV, 33 panels"},{"id":"BP-21DA58D4","address":"14355 Flagler St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.713048,"lng":-80.218408,"contractor":"Solar Energy Management","applied":"2026-01-09","description":"8.1kW roof-mount solar PV, 20 panels"},{"id":"BP-B146BE70","address":"4099 Brickell Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Final","lat":25.704921,"lng":-80.243709,"contractor":"Florida Power Services","applied":"2026-02-27","description":"10.3kW roof-mount solar PV, 25 panels"},{"id":"BP-5391AC00","address":"5682 NE 2nd Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.766219,"lng":-80.196967,"contractor":"Goldin Solar","applied":"2026-04-24","description":"13.3kW roof-mount solar PV, 33 panels"},{"id":"BP-75748B08","address":"8904 NE 2nd Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"On Hold","lat":25.791028,"lng":-80.233547,"contractor":"Sun Tree Solar Energy","applied":"2025-12-27","description":"6.1kW roof-mount solar PV, 15 panels"},{"id":"BP-D0FE4EA5","address":"13190 NE 2nd Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.731915,"lng":-80.171506,"contractor":"Goldin Solar","applied":"2026-02-13","description":"13.3kW roof-mount solar PV, 33 panels"},{"id":"BP-3E7A08F7","address":"20727 Flagler St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.787913,"lng":-80.150681,"contractor":"EcoView Solar","applied":"2026-02-21","description":"12.6kW roof-mount solar PV, 31 panels"},{"id":"BP-46059F4A","address":"4535 Calle Ocho, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Final","lat":25.704495,"lng":-80.164332,"contractor":"Sun Tree Solar Energy","applied":"2026-03-30","description":"11.0kW roof-mount solar PV, 27 panels"},{"id":"BP-C174BC6F","address":"25327 SW 8th St, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.740998,"lng":-80.166005,"contractor":"Sun Tree Solar Energy","applied":"2026-02-08","description":"9.1kW roof-mount solar PV, 22 panels"},{"id":"BP-7E93B86D","address":"25475 Bird Rd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.702106,"lng":-80.188576,"contractor":"Cutting Edge Solar","applied":"2026-04-08","description":"12.5kW roof-mount solar PV, 31 panels"},{"id":"BP-5D8862C1","address":"10740 Coconut Grove Dr, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.757672,"lng":-80.144155,"contractor":"A1A Solar Contracting","applied":"2026-03-11","description":"5.8kW roof-mount solar PV, 14 panels"},{"id":"BP-760648FE","address":"18988 Biscayne Blvd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.781171,"lng":-80.197901,"contractor":"Cutting Edge Solar","applied":"2026-03-07","description":"8.1kW roof-mount solar PV, 20 panels"},{"id":"BP-FEBC342C","address":"13134 Calle Ocho, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.778352,"lng":-80.200296,"contractor":"Florida Power Services","applied":"2026-02-24","description":"12.0kW roof-mount solar PV, 30 panels"},{"id":"BP-B39F4AF6","address":"16007 Bird Rd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.742306,"lng":-80.138453,"contractor":"A1A Solar Contracting","applied":"2026-04-23","description":"10.1kW roof-mount solar PV, 25 panels"},{"id":"BP-A1F4A6D2","address":"2234 Coral Way, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.791683,"lng":-80.23563,"contractor":"Goldin Solar","applied":"2026-02-14","description":"9.3kW roof-mount solar PV, 23 panels"},{"id":"BP-DB7CAE42","address":"8176 Coconut Grove Dr, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.792667,"lng":-80.188223,"contractor":"Cutting Edge Solar","applied":"2026-01-30","description":"8.1kW roof-mount solar PV, 20 panels"},{"id":"BP-1A71205D","address":"20936 Brickell Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.717444,"lng":-80.156663,"contractor":"Sun Tree Solar Energy","applied":"2026-03-14","description":"6.9kW roof-mount solar PV, 17 panels"},{"id":"BP-EBA618B3","address":"21224 NE 2nd Ave, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.789753,"lng":-80.161581,"contractor":"EcoView Solar","applied":"2026-04-19","description":"12.2kW roof-mount solar PV, 30 panels"},{"id":"BP-686C0311","address":"23115 Calle Ocho, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Issued","lat":25.794712,"lng":-80.237747,"contractor":"Florida Power Services","applied":"2026-03-03","description":"7.0kW roof-mount solar PV, 17 panels"},{"id":"BP-222CDCBF","address":"22107 Bird Rd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.705894,"lng":-80.224961,"contractor":"Sunshine State Solar","applied":"2026-03-05","description":"9.3kW roof-mount solar PV, 23 panels"},{"id":"BP-661A5FCA","address":"25372 Coral Way, Miami, FL","city":"Miami","county":"Miami-Dade","status":"In Review","lat":25.732671,"lng":-80.204341,"contractor":"Florida Power Services","applied":"2026-04-03","description":"6.2kW roof-mount solar PV, 15 panels"},{"id":"BP-3A689B4B","address":"24844 Biscayne Blvd, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.804005,"lng":-80.187051,"contractor":"EcoView Solar","applied":"2026-02-07","description":"5.4kW roof-mount solar PV, 13 panels"},{"id":"BP-BAF91B07","address":"328 Coconut Grove Dr, Miami, FL","city":"Miami","county":"Miami-Dade","status":"Pending","lat":25.721296,"lng":-80.230589,"contractor":"Brilliant Harvest Solar","applied":"2026-02-24","description":"13.6kW roof-mount solar PV, 34 panels"}],"fort-myers":[{"id":"BP-42CC7B5D","address":"26476 Daniels Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.670396,"lng":-81.929438,"contractor":"ESA Energy Savings Advisors","applied":"2026-03-30","description":"7.4kW roof-mount solar PV, 18 panels"},{"id":"BP-4C56BCAF","address":"710 McGregor Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Pending","lat":26.62538,"lng":-81.884835,"contractor":"Titan Solar Power","applied":"2026-02-18","description":"9.7kW roof-mount solar PV, 24 panels"},{"id":"BP-A0B0696D","address":"21783 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.668301,"lng":-81.915349,"contractor":"PosiGen Solar","applied":"2026-02-19","description":"11.9kW roof-mount solar PV, 29 panels"},{"id":"BP-95BB2F9D","address":"24518 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.603516,"lng":-81.828818,"contractor":"Sunrun Installation Services","applied":"2026-01-02","description":"9.9kW roof-mount solar PV, 24 panels"},{"id":"BP-825DC52C","address":"12112 McGregor Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.66602,"lng":-81.850884,"contractor":"Trinity Solar FL","applied":"2026-04-23","description":"7.7kW roof-mount solar PV, 19 panels"},{"id":"BP-3A8E464A","address":"18439 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.639337,"lng":-81.869475,"contractor":"Blue Raven Solar","applied":"2026-02-03","description":"6.5kW roof-mount solar PV, 16 panels"},{"id":"BP-967082F3","address":"19545 Winkler Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Final","lat":26.597312,"lng":-81.850801,"contractor":"Freedom Solar Services","applied":"2026-02-10","description":"8.0kW roof-mount solar PV, 20 panels"},{"id":"BP-B500E907","address":"5850 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"On Hold","lat":26.631439,"lng":-81.886257,"contractor":"Blue Raven Solar","applied":"2026-02-27","description":"9.5kW roof-mount solar PV, 23 panels"},{"id":"BP-2501BEBF","address":"18426 McGregor Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"On Hold","lat":26.656839,"lng":-81.881366,"contractor":"MomentumSolar FL","applied":"2026-01-18","description":"6.0kW roof-mount solar PV, 15 panels"},{"id":"BP-3A8FBC17","address":"18523 Colonial Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.625468,"lng":-81.857417,"contractor":"Freedom Solar Services","applied":"2026-02-01","description":"9.7kW roof-mount solar PV, 24 panels"},{"id":"BP-DF452194","address":"22212 Daniels Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.648962,"lng":-81.894179,"contractor":"Solar Source Florida","applied":"2026-04-17","description":"10.2kW roof-mount solar PV, 25 panels"},{"id":"BP-5893B692","address":"1725 Edison Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.634029,"lng":-81.863388,"contractor":"Blue Raven Solar","applied":"2026-04-24","description":"7.0kW roof-mount solar PV, 17 panels"},{"id":"BP-32C08181","address":"4460 Winkler Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.606978,"lng":-81.847071,"contractor":"SunPower of SW Florida","applied":"2026-01-10","description":"8.1kW roof-mount solar PV, 20 panels"},{"id":"BP-70598B20","address":"14025 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Final","lat":26.639552,"lng":-81.822243,"contractor":"Trinity Solar FL","applied":"2025-12-31","description":"12.9kW roof-mount solar PV, 32 panels"},{"id":"BP-4F25EF87","address":"11920 Winkler Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Pending","lat":26.595936,"lng":-81.876368,"contractor":"PosiGen Solar","applied":"2026-01-15","description":"11.7kW roof-mount solar PV, 29 panels"},{"id":"BP-9D15F32D","address":"26934 McGregor Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Pending","lat":26.655851,"lng":-81.830193,"contractor":"Sunrun Installation Services","applied":"2026-04-11","description":"9.9kW roof-mount solar PV, 24 panels"},{"id":"BP-FB13F3C4","address":"11116 Winkler Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Pending","lat":26.634551,"lng":-81.867941,"contractor":"Trinity Solar FL","applied":"2026-03-25","description":"11.7kW roof-mount solar PV, 29 panels"},{"id":"BP-7D0FD9BF","address":"16415 Hanson St, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Issued","lat":26.612194,"lng":-81.909454,"contractor":"Titan Solar Power","applied":"2026-04-02","description":"11.0kW roof-mount solar PV, 27 panels"},{"id":"BP-DB14F753","address":"5176 Daniels Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Final","lat":26.667747,"lng":-81.882396,"contractor":"Sunrun Installation Services","applied":"2026-02-17","description":"5.7kW roof-mount solar PV, 14 panels"},{"id":"BP-92AD0DEF","address":"27647 Daniels Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Final","lat":26.649814,"lng":-81.907254,"contractor":"Blue Raven Solar","applied":"2025-12-29","description":"7.8kW roof-mount solar PV, 19 panels"},{"id":"BP-4428C66F","address":"8963 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Final","lat":26.654077,"lng":-81.894889,"contractor":"MomentumSolar FL","applied":"2026-03-15","description":"6.5kW roof-mount solar PV, 16 panels"},{"id":"BP-CEFC59E0","address":"1899 Cleveland Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Pending","lat":26.691974,"lng":-81.864792,"contractor":"ESA Energy Savings Advisors","applied":"2026-02-23","description":"8.8kW roof-mount solar PV, 22 panels"},{"id":"BP-9EFC35F8","address":"27071 Colonial Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.656544,"lng":-81.86681,"contractor":"Gulf Coast Renewables Inc","applied":"2026-02-15","description":"13.8kW roof-mount solar PV, 34 panels"},{"id":"BP-6A9D10EB","address":"10257 Colonial Blvd, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.689964,"lng":-81.906161,"contractor":"Blue Raven Solar","applied":"2026-03-05","description":"12.1kW roof-mount solar PV, 30 panels"},{"id":"BP-2E54319A","address":"21227 Six Mile Cypress Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"Pending","lat":26.627469,"lng":-81.8169,"contractor":"Blue Raven Solar","applied":"2026-01-20","description":"10.4kW roof-mount solar PV, 26 panels"},{"id":"BP-7A0A9085","address":"28656 Cleveland Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.692489,"lng":-81.837035,"contractor":"Solar Source Florida","applied":"2025-12-30","description":"10.1kW roof-mount solar PV, 25 panels"},{"id":"BP-26D8FB77","address":"1780 Daniels Pkwy, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.633408,"lng":-81.890478,"contractor":"Trinity Solar FL","applied":"2026-04-03","description":"7.8kW roof-mount solar PV, 19 panels"},{"id":"BP-E7E8E1B4","address":"13494 Cleveland Ave, Fort Myers, FL","city":"Fort Myers","county":"Lee","status":"In Review","lat":26.580954,"lng":-81.84332,"contractor":"SunPower of SW Florida","applied":"2026-02-08","description":"9.6kW roof-mount solar PV, 24 panels"}],"naples":[{"id":"BP-B7C2AF63","address":"18406 Airport Pulling Rd, Naples, FL","city":"Naples","county":"Collier","status":"In Review","lat":26.169155,"lng":-81.770974,"contractor":"Trinity Solar FL","applied":"2026-04-11","description":"6.9kW roof-mount solar PV, 17 panels"},{"id":"BP-822754EE","address":"23160 5th Ave S, Naples, FL","city":"Naples","county":"Collier","status":"Final","lat":26.1812,"lng":-81.754579,"contractor":"Gulf Coast Renewables Inc","applied":"2026-01-09","description":"11.4kW roof-mount solar PV, 28 panels"},{"id":"BP-3DF5F3D3","address":"26032 5th Ave S, Naples, FL","city":"Naples","county":"Collier","status":"Final","lat":26.129874,"lng":-81.783972,"contractor":"ESA Energy Savings Advisors","applied":"2025-12-27","description":"4.7kW roof-mount solar PV, 11 panels"},{"id":"BP-F9BDFC13","address":"13049 Vanderbilt Beach Rd, Naples, FL","city":"Naples","county":"Collier","status":"Final","lat":26.088682,"lng":-81.835543,"contractor":"Trinity Solar FL","applied":"2026-04-08","description":"8.0kW roof-mount solar PV, 20 panels"},{"id":"BP-8D658428","address":"12851 Airport Pulling Rd, Naples, FL","city":"Naples","county":"Collier","status":"On Hold","lat":26.132271,"lng":-81.802582,"contractor":"Solar Source Florida","applied":"2026-01-02","description":"7.0kW roof-mount solar PV, 17 panels"},{"id":"BP-290182D6","address":"28920 Immokalee Rd, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.090809,"lng":-81.760167,"contractor":"Solar Source Florida","applied":"2026-01-09","description":"6.1kW roof-mount solar PV, 15 panels"},{"id":"BP-DAEC2A8B","address":"26559 Tamiami Trl N, Naples, FL","city":"Naples","county":"Collier","status":"Final","lat":26.145515,"lng":-81.798102,"contractor":"SunPower of SW Florida","applied":"2026-01-20","description":"9.7kW roof-mount solar PV, 24 panels"},{"id":"BP-4A25C73E","address":"22388 Golden Gate Pkwy, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.195526,"lng":-81.793511,"contractor":"Titan Solar Power","applied":"2026-04-13","description":"4.6kW roof-mount solar PV, 11 panels"},{"id":"BP-0F5E8A46","address":"14281 Golden Gate Pkwy, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.142741,"lng":-81.759174,"contractor":"MomentumSolar FL","applied":"2026-01-15","description":"13.6kW roof-mount solar PV, 34 panels"},{"id":"BP-CB04BEEB","address":"18981 Vanderbilt Beach Rd, Naples, FL","city":"Naples","county":"Collier","status":"Final","lat":26.104787,"lng":-81.821922,"contractor":"MomentumSolar FL","applied":"2026-04-04","description":"13.5kW roof-mount solar PV, 33 panels"},{"id":"BP-465A83FB","address":"2253 5th Ave S, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.116458,"lng":-81.83648,"contractor":"SunPower of SW Florida","applied":"2026-02-25","description":"13.9kW roof-mount solar PV, 34 panels"},{"id":"BP-2307AC76","address":"6035 Goodlette Frank Rd, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.118273,"lng":-81.852781,"contractor":"Titan Solar Power","applied":"2026-01-26","description":"11.1kW roof-mount solar PV, 27 panels"},{"id":"BP-7FB81262","address":"3135 Immokalee Rd, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.194191,"lng":-81.790101,"contractor":"MomentumSolar FL","applied":"2026-01-28","description":"8.5kW roof-mount solar PV, 21 panels"},{"id":"BP-3CC391B8","address":"16544 Immokalee Rd, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.139987,"lng":-81.769997,"contractor":"ESA Energy Savings Advisors","applied":"2026-04-24","description":"5.9kW roof-mount solar PV, 14 panels"},{"id":"BP-47715AD7","address":"25386 Pine Ridge Rd, Naples, FL","city":"Naples","county":"Collier","status":"In Review","lat":26.18781,"lng":-81.823469,"contractor":"Titan Solar Power","applied":"2026-02-19","description":"7.2kW roof-mount solar PV, 18 panels"},{"id":"BP-6AEB9B6A","address":"27520 Immokalee Rd, Naples, FL","city":"Naples","county":"Collier","status":"Issued","lat":26.15142,"lng":-81.836627,"contractor":"PosiGen Solar","applied":"2026-04-09","description":"6.6kW roof-mount solar PV, 16 panels"},{"id":"BP-9A331A88","address":"18956 Tamiami Trl N, Naples, FL","city":"Naples","county":"Collier","status":"Issued","lat":26.150111,"lng":-81.786269,"contractor":"Gulf Coast Renewables Inc","applied":"2026-04-20","description":"7.9kW roof-mount solar PV, 19 panels"},{"id":"BP-CCB6FFC3","address":"5539 5th Ave S, Naples, FL","city":"Naples","county":"Collier","status":"On Hold","lat":26.139431,"lng":-81.766484,"contractor":"Titan Solar Power","applied":"2026-04-01","description":"8.6kW roof-mount solar PV, 21 panels"},{"id":"BP-592D999C","address":"12175 5th Ave S, Naples, FL","city":"Naples","county":"Collier","status":"In Review","lat":26.201628,"lng":-81.774245,"contractor":"Sunrun Installation Services","applied":"2026-04-01","description":"12.0kW roof-mount solar PV, 30 panels"},{"id":"BP-72B2FAAF","address":"9683 Tamiami Trl N, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.143303,"lng":-81.746119,"contractor":"Solar Source Florida","applied":"2026-04-22","description":"4.7kW roof-mount solar PV, 11 panels"},{"id":"BP-BC9FE7A0","address":"23393 Pine Ridge Rd, Naples, FL","city":"Naples","county":"Collier","status":"Issued","lat":26.191509,"lng":-81.848814,"contractor":"PosiGen Solar","applied":"2026-01-16","description":"8.7kW roof-mount solar PV, 21 panels"},{"id":"BP-39DF7535","address":"16554 Tamiami Trl N, Naples, FL","city":"Naples","county":"Collier","status":"Pending","lat":26.119526,"lng":-81.756717,"contractor":"ESA Energy Savings Advisors","applied":"2026-04-22","description":"6.7kW roof-mount solar PV, 16 panels"},{"id":"BP-744E1ABA","address":"24330 Pine Ridge Rd, Naples, FL","city":"Naples","county":"Collier","status":"In Review","lat":26.201172,"lng":-81.77166,"contractor":"SunPower of SW Florida","applied":"2026-02-14","description":"5.0kW roof-mount solar PV, 12 panels"},{"id":"BP-761DA1D2","address":"6533 Pine Ridge Rd, Naples, FL","city":"Naples","county":"Collier","status":"Final","lat":26.151399,"lng":-81.833647,"contractor":"Solar Source Florida","applied":"2026-04-01","description":"11.8kW roof-mount solar PV, 29 panels"}],"bonita-springs":[{"id":"BP-9D9AF706","address":"19934 Bonita Grande Dr, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"On Hold","lat":26.3418,"lng":-81.835974,"contractor":"Titan Solar Power","applied":"2026-02-23","description":"13.8kW roof-mount solar PV, 34 panels"},{"id":"BP-2A1F51BD","address":"4480 Coconut Rd, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.373276,"lng":-81.761238,"contractor":"MomentumSolar FL","applied":"2026-03-19","description":"6.2kW roof-mount solar PV, 15 panels"},{"id":"BP-DCB164A6","address":"2930 Bonita Beach Rd, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"On Hold","lat":26.353601,"lng":-81.82388,"contractor":"MomentumSolar FL","applied":"2026-03-31","description":"13.1kW roof-mount solar PV, 32 panels"},{"id":"BP-3E5DEB14","address":"10896 Terry St, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.342958,"lng":-81.766139,"contractor":"ESA Energy Savings Advisors","applied":"2026-03-14","description":"7.5kW roof-mount solar PV, 18 panels"},{"id":"BP-BFBFFA7C","address":"7816 Coconut Rd, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"In Review","lat":26.32533,"lng":-81.802051,"contractor":"Sunrun Installation Services","applied":"2026-03-02","description":"9.8kW roof-mount solar PV, 24 panels"},{"id":"BP-4262E517","address":"7874 Imperial Pkwy, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Pending","lat":26.287715,"lng":-81.773098,"contractor":"PosiGen Solar","applied":"2026-03-05","description":"10.8kW roof-mount solar PV, 27 panels"},{"id":"BP-38F4DE87","address":"2646 Old US 41, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"In Review","lat":26.379117,"lng":-81.798118,"contractor":"Gulf Coast Renewables Inc","applied":"2026-02-27","description":"6.2kW roof-mount solar PV, 15 panels"},{"id":"BP-A083D1A8","address":"7995 Bonita Beach Rd, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.324801,"lng":-81.834622,"contractor":"PosiGen Solar","applied":"2025-12-26","description":"9.5kW roof-mount solar PV, 23 panels"},{"id":"BP-3B58F8B9","address":"11438 Bonita Grande Dr, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"In Review","lat":26.371198,"lng":-81.770084,"contractor":"Solar Source Florida","applied":"2026-01-30","description":"11.2kW roof-mount solar PV, 28 panels"},{"id":"BP-B9C37F9B","address":"14778 Terry St, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.320508,"lng":-81.771699,"contractor":"Freedom Solar Services","applied":"2026-02-15","description":"11.4kW roof-mount solar PV, 28 panels"},{"id":"BP-8BEFC184","address":"26766 Bonita Grande Dr, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.309858,"lng":-81.735349,"contractor":"SunPower of SW Florida","applied":"2026-02-10","description":"11.0kW roof-mount solar PV, 27 panels"},{"id":"BP-354DA989","address":"16255 Terry St, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.280876,"lng":-81.790076,"contractor":"Solar Source Florida","applied":"2026-03-24","description":"11.4kW roof-mount solar PV, 28 panels"},{"id":"BP-717497EB","address":"10450 Old US 41, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.339306,"lng":-81.757117,"contractor":"Florida Solar Energy LLC","applied":"2026-01-04","description":"5.5kW roof-mount solar PV, 13 panels"},{"id":"BP-2B7375B3","address":"22725 Old US 41, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.345815,"lng":-81.824219,"contractor":"SunPower of SW Florida","applied":"2026-01-06","description":"13.2kW roof-mount solar PV, 33 panels"},{"id":"BP-54634FD8","address":"27001 Bonita Grande Dr, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"In Review","lat":26.34607,"lng":-81.772453,"contractor":"Gulf Coast Renewables Inc","applied":"2026-02-04","description":"12.7kW roof-mount solar PV, 31 panels"},{"id":"BP-889B20B4","address":"16807 Coconut Rd, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.297571,"lng":-81.802821,"contractor":"Trinity Solar FL","applied":"2026-03-10","description":"13.5kW roof-mount solar PV, 33 panels"},{"id":"BP-35F35430","address":"3398 Bonita Grande Dr, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Pending","lat":26.288291,"lng":-81.802289,"contractor":"Titan Solar Power","applied":"2026-04-01","description":"10.8kW roof-mount solar PV, 27 panels"},{"id":"BP-5B0F3B54","address":"4764 Imperial Pkwy, Bonita Springs, FL","city":"Bonita Springs","county":"Lee","status":"Issued","lat":26.297355,"lng":-81.728453,"contractor":"Sunrun Installation Services","applied":"2026-03-20","description":"11.1kW roof-mount solar PV, 27 panels"}],"north-fort-myers":[{"id":"BP-CCCDF369","address":"6593 Hart Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Pending","lat":26.695581,"lng":-81.842766,"contractor":"ESA Energy Savings Advisors","applied":"2026-02-14","description":"7.5kW roof-mount solar PV, 18 panels"},{"id":"BP-71E7D047","address":"4627 Pondella Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Issued","lat":26.7246,"lng":-81.901766,"contractor":"Sunrun Installation Services","applied":"2026-03-08","description":"9.8kW roof-mount solar PV, 24 panels"},{"id":"BP-462D9266","address":"14775 Slater Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"In Review","lat":26.709147,"lng":-81.878649,"contractor":"Titan Solar Power","applied":"2026-01-29","description":"12.0kW roof-mount solar PV, 30 panels"},{"id":"BP-03B3FD80","address":"19521 Pondella Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Issued","lat":26.620472,"lng":-81.836128,"contractor":"Blue Raven Solar","applied":"2026-03-12","description":"5.6kW roof-mount solar PV, 14 panels"},{"id":"BP-386D4120","address":"15560 Bayshore Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Pending","lat":26.688773,"lng":-81.882128,"contractor":"Sunrun Installation Services","applied":"2026-04-03","description":"4.9kW roof-mount solar PV, 12 panels"},{"id":"BP-EDC85767","address":"13006 Orange Grove Blvd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Pending","lat":26.704434,"lng":-81.843861,"contractor":"Freedom Solar Services","applied":"2026-01-03","description":"6.0kW roof-mount solar PV, 15 panels"},{"id":"BP-6D80511A","address":"21847 Orange Grove Blvd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"On Hold","lat":26.686259,"lng":-81.898818,"contractor":"Blue Raven Solar","applied":"2026-04-04","description":"8.4kW roof-mount solar PV, 21 panels"},{"id":"BP-88136119","address":"6998 Bayshore Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Issued","lat":26.707144,"lng":-81.88109,"contractor":"Gulf Coast Renewables Inc","applied":"2026-04-20","description":"6.8kW roof-mount solar PV, 17 panels"},{"id":"BP-2706DAD2","address":"24614 Hart Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"In Review","lat":26.686338,"lng":-81.917088,"contractor":"ESA Energy Savings Advisors","applied":"2026-01-30","description":"11.3kW roof-mount solar PV, 28 panels"},{"id":"BP-B2F38555","address":"6113 Hancock Bridge Pkwy, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Pending","lat":26.663527,"lng":-81.862507,"contractor":"Gulf Coast Renewables Inc","applied":"2026-02-25","description":"12.7kW roof-mount solar PV, 31 panels"},{"id":"BP-CD3FB305","address":"116 Pondella Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"In Review","lat":26.723411,"lng":-81.884442,"contractor":"ESA Energy Savings Advisors","applied":"2026-01-27","description":"10.2kW roof-mount solar PV, 25 panels"},{"id":"BP-92CAFCBF","address":"24733 Slater Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Pending","lat":26.622354,"lng":-81.870049,"contractor":"PosiGen Solar","applied":"2025-12-27","description":"13.0kW roof-mount solar PV, 32 panels"},{"id":"BP-1BE8CFB8","address":"24843 Orange Grove Blvd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Final","lat":26.699019,"lng":-81.869838,"contractor":"PosiGen Solar","applied":"2026-02-07","description":"7.6kW roof-mount solar PV, 19 panels"},{"id":"BP-B1D62E73","address":"13586 Hart Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Pending","lat":26.729951,"lng":-81.908636,"contractor":"Gulf Coast Renewables Inc","applied":"2026-03-03","description":"14.0kW roof-mount solar PV, 35 panels"},{"id":"BP-3E880185","address":"9211 Hart Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"On Hold","lat":26.613554,"lng":-81.880169,"contractor":"Solar Source Florida","applied":"2026-02-19","description":"8.5kW roof-mount solar PV, 21 panels"},{"id":"BP-D73C1E2C","address":"2710 Pine Island Rd, North Fort Myers, FL","city":"North Fort Myers","county":"Lee","status":"Final","lat":26.633238,"lng":-81.935656,"contractor":"MomentumSolar FL","applied":"2026-02-01","description":"12.6kW roof-mount solar PV, 31 panels"}],"port-charlotte":[{"id":"BP-B22D6FB6","address":"16659 Cochran Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":27.011142,"lng":-82.093251,"contractor":"Trinity Solar FL","applied":"2026-01-23","description":"8.5kW roof-mount solar PV system w/ 21 panels"},{"id":"BP-22091909","address":"25431 Cochran Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Final","lat":26.973627,"lng":-82.151025,"contractor":"Charlotte Solar & Roofing","applied":"2026-03-26","description":"7.1kW roof-mount solar PV system w/ 17 panels"},{"id":"BP-C19227CA","address":"23097 Conway Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":27.051299,"lng":-82.082836,"contractor":"Gulf Coast Renewables Inc","applied":"2026-02-06","description":"6.1kW roof-mount solar PV system w/ 15 panels"},{"id":"BP-9DFE4661","address":"16796 Quesada Ave, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":26.998122,"lng":-82.069906,"contractor":"Blue Raven Solar","applied":"2026-01-04","description":"10.5kW roof-mount solar PV system w/ 26 panels"},{"id":"BP-8EE31527","address":"17438 Aaron St, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":26.96907,"lng":-82.094213,"contractor":"Trinity Solar FL","applied":"2026-04-23","description":"11.0kW roof-mount solar PV system w/ 27 panels"},{"id":"BP-62FA1BCA","address":"5282 Veterans Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":26.993347,"lng":-82.046142,"contractor":"MomentumSolar FL","applied":"2026-01-02","description":"11.7kW roof-mount solar PV system w/ 29 panels"},{"id":"BP-55E7B54D","address":"5108 Olean Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Final","lat":26.98377,"lng":-82.141214,"contractor":"ESA Energy Savings Advisors","applied":"2026-01-15","description":"10.2kW roof-mount solar PV system w/ 25 panels"},{"id":"BP-A1132F10","address":"28870 Cochran Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":27.006983,"lng":-82.151149,"contractor":"Charlotte Solar & Roofing","applied":"2026-01-21","description":"5.2kW roof-mount solar PV system w/ 13 panels"},{"id":"BP-BC1FD194","address":"14894 Deep Creek Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":26.953421,"lng":-82.133636,"contractor":"SunPower of SW Florida","applied":"2026-03-12","description":"9.8kW roof-mount solar PV system w/ 24 panels"},{"id":"BP-4F45E960","address":"29768 Loveland Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":26.94267,"lng":-82.120949,"contractor":"PosiGen Solar","applied":"2026-02-18","description":"10.9kW roof-mount solar PV system w/ 27 panels"},{"id":"BP-E3466192","address":"26560 Appleton Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":26.987747,"lng":-82.149281,"contractor":"MomentumSolar FL","applied":"2026-01-30","description":"8.5kW roof-mount solar PV system w/ 21 panels"},{"id":"BP-746A5DBF","address":"23962 Chamberlain Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":26.979616,"lng":-82.057199,"contractor":"Freedom Solar Services","applied":"2026-03-24","description":"9.6kW roof-mount solar PV system w/ 24 panels"},{"id":"BP-125520AA","address":"7104 Appleton Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":27.042658,"lng":-82.052307,"contractor":"Freedom Solar Services","applied":"2026-04-03","description":"13.9kW roof-mount solar PV system w/ 34 panels"},{"id":"BP-5CDB6EFD","address":"16577 Appleton Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"On Hold","lat":27.049226,"lng":-82.096865,"contractor":"SunPower of SW Florida","applied":"2026-04-17","description":"5.3kW roof-mount solar PV system w/ 13 panels"},{"id":"BP-276D49B9","address":"19070 Cochran Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":27.010242,"lng":-82.086274,"contractor":"MomentumSolar FL","applied":"2026-03-02","description":"9.5kW roof-mount solar PV system w/ 23 panels"},{"id":"BP-77EBD409","address":"4388 Chamberlain Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Final","lat":27.019503,"lng":-82.1246,"contractor":"SunPower of SW Florida","applied":"2026-03-15","description":"4.6kW roof-mount solar PV system w/ 11 panels"},{"id":"BP-0B8BFBBE","address":"4440 Conway Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":27.050891,"lng":-82.054896,"contractor":"PosiGen Solar","applied":"2026-01-02","description":"7.2kW roof-mount solar PV system w/ 18 panels"},{"id":"BP-BAE1178C","address":"17977 Quesada Ave, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":26.943223,"lng":-82.116294,"contractor":"ESA Energy Savings Advisors","applied":"2026-02-13","description":"5.7kW roof-mount solar PV system w/ 14 panels"},{"id":"BP-98F54E3A","address":"11689 Harbor Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"On Hold","lat":27.032514,"lng":-82.054504,"contractor":"Charlotte Solar & Roofing","applied":"2026-03-03","description":"11.6kW roof-mount solar PV system w/ 29 panels"},{"id":"BP-9A55A485","address":"28234 Edgewater Dr, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":26.995383,"lng":-82.136651,"contractor":"Gulf Coast Renewables Inc","applied":"2025-12-28","description":"7.4kW roof-mount solar PV system w/ 18 panels"},{"id":"BP-2F7551C5","address":"9229 Peachland Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":27.042622,"lng":-82.044573,"contractor":"ESA Energy Savings Advisors","applied":"2026-03-20","description":"9.3kW roof-mount solar PV system w/ 23 panels"},{"id":"BP-75F7F0DA","address":"8446 Olean Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Final","lat":26.944226,"lng":-82.108273,"contractor":"ESA Energy Savings Advisors","applied":"2026-02-17","description":"11.0kW roof-mount solar PV system w/ 27 panels"},{"id":"BP-5E23B33A","address":"13877 Olean Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Final","lat":27.018692,"lng":-82.115103,"contractor":"Freedom Solar Services","applied":"2026-01-19","description":"9.9kW roof-mount solar PV system w/ 24 panels"},{"id":"BP-09F77A09","address":"15336 Peachland Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":26.991914,"lng":-82.079525,"contractor":"MomentumSolar FL","applied":"2026-02-18","description":"13.1kW roof-mount solar PV system w/ 32 panels"},{"id":"BP-FF35B1E0","address":"3160 Peachland Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Pending","lat":27.037111,"lng":-82.070463,"contractor":"Gulf Coast Renewables Inc","applied":"2026-01-28","description":"12.2kW roof-mount solar PV system w/ 30 panels"},{"id":"BP-A516370D","address":"27620 Cochran Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":27.015419,"lng":-82.068702,"contractor":"Gulf Coast Renewables Inc","applied":"2026-02-17","description":"6.8kW roof-mount solar PV system w/ 17 panels"},{"id":"BP-6D97446E","address":"4634 Loveland Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":26.957,"lng":-82.114636,"contractor":"Solar Source Florida","applied":"2026-04-05","description":"8.4kW roof-mount solar PV system w/ 21 panels"},{"id":"BP-6555DFE1","address":"16098 Cochran Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":26.965231,"lng":-82.1083,"contractor":"Titan Solar Power","applied":"2026-04-21","description":"10.9kW roof-mount solar PV system w/ 27 panels"},{"id":"BP-2AB4EFA9","address":"19495 Chamberlain Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":27.006627,"lng":-82.157348,"contractor":"Solar Source Florida","applied":"2026-02-01","description":"12.7kW roof-mount solar PV system w/ 31 panels"},{"id":"BP-86A6C282","address":"25043 Peachland Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"In Review","lat":27.044457,"lng":-82.127209,"contractor":"Florida Solar Energy LLC","applied":"2026-01-08","description":"12.4kW roof-mount solar PV system w/ 31 panels"},{"id":"BP-30CD4FC0","address":"15338 Olean Blvd, Port Charlotte, FL","city":"Port Charlotte","status":"Issued","lat":27.022836,"lng":-82.068572,"contractor":"SunPower of SW Florida","applied":"2026-04-03","description":"11.9kW roof-mount solar PV system w/ 29 panels"}],"north-port":[{"id":"BP-1CD68C88","address":"24399 Price Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.017204,"lng":-82.269115,"contractor":"Solar Source Florida","applied":"2026-01-20","description":"11.5kW roof-mount solar PV system w/ 28 panels"},{"id":"BP-D2B06F2A","address":"9205 S Cranberry Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.002858,"lng":-82.181034,"contractor":"Blue Raven Solar","applied":"2026-03-12","description":"8.1kW roof-mount solar PV system w/ 20 panels"},{"id":"BP-DF5F111F","address":"4190 Salford Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.100974,"lng":-82.250476,"contractor":"Blue Raven Solar","applied":"2026-02-13","description":"10.5kW roof-mount solar PV system w/ 26 panels"},{"id":"BP-C5B98491","address":"1932 Tropicaire Blvd, North Port, FL","city":"North Port","status":"In Review","lat":27.011686,"lng":-82.292048,"contractor":"PosiGen Solar","applied":"2026-03-15","description":"5.1kW roof-mount solar PV system w/ 12 panels"},{"id":"BP-E3CEF1EF","address":"29089 Pan American Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.093946,"lng":-82.240838,"contractor":"Solar Source Florida","applied":"2026-03-22","description":"11.6kW roof-mount solar PV system w/ 29 panels"},{"id":"BP-DCCF8435","address":"8785 Sumter Blvd, North Port, FL","city":"North Port","status":"Final","lat":27.047521,"lng":-82.223109,"contractor":"Solar Source Florida","applied":"2026-03-28","description":"11.4kW roof-mount solar PV system w/ 28 panels"},{"id":"BP-3B1B4046","address":"14620 Biscayne Dr, North Port, FL","city":"North Port","status":"Pending","lat":27.081163,"lng":-82.193184,"contractor":"Trinity Solar FL","applied":"2026-04-12","description":"14.0kW roof-mount solar PV system w/ 35 panels"},{"id":"BP-512B423E","address":"18311 Tropicaire Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.063625,"lng":-82.237499,"contractor":"Florida Solar Energy LLC","applied":"2026-03-31","description":"13.7kW roof-mount solar PV system w/ 34 panels"},{"id":"BP-DA7AC8EA","address":"21529 Tropicaire Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.047673,"lng":-82.215756,"contractor":"Freedom Solar Services","applied":"2026-02-13","description":"10.8kW roof-mount solar PV system w/ 27 panels"},{"id":"BP-85BCC0B5","address":"9024 Sumter Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.018011,"lng":-82.270624,"contractor":"Freedom Solar Services","applied":"2026-03-12","description":"10.5kW roof-mount solar PV system w/ 26 panels"},{"id":"BP-9BC6133B","address":"9166 Dale Ave, North Port, FL","city":"North Port","status":"Issued","lat":26.98949,"lng":-82.255873,"contractor":"Sunrun Installation Services","applied":"2026-04-08","description":"6.0kW roof-mount solar PV system w/ 15 panels"},{"id":"BP-C6B08BCC","address":"5977 Price Blvd, North Port, FL","city":"North Port","status":"In Review","lat":27.072588,"lng":-82.256038,"contractor":"Freedom Solar Services","applied":"2025-12-26","description":"10.9kW roof-mount solar PV system w/ 27 panels"},{"id":"BP-A59DCA7B","address":"5951 Chamberlain Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.053871,"lng":-82.177874,"contractor":"Solar Source Florida","applied":"2026-04-20","description":"8.6kW roof-mount solar PV system w/ 21 panels"},{"id":"BP-0F750DC4","address":"10919 Greenwood Ave, North Port, FL","city":"North Port","status":"Issued","lat":27.058979,"lng":-82.216294,"contractor":"Solar Source Florida","applied":"2026-04-09","description":"9.3kW roof-mount solar PV system w/ 23 panels"},{"id":"BP-74FD5659","address":"15023 Biscayne Dr, North Port, FL","city":"North Port","status":"Issued","lat":27.033933,"lng":-82.220328,"contractor":"Trinity Solar FL","applied":"2026-03-31","description":"9.2kW roof-mount solar PV system w/ 23 panels"},{"id":"BP-5A48D539","address":"5863 Toledo Blade Blvd, North Port, FL","city":"North Port","status":"Pending","lat":27.080693,"lng":-82.212391,"contractor":"Charlotte Solar & Roofing","applied":"2026-02-24","description":"6.9kW roof-mount solar PV system w/ 17 panels"},{"id":"BP-6D2255EE","address":"19611 Salford Blvd, North Port, FL","city":"North Port","status":"Issued","lat":27.022276,"lng":-82.20527,"contractor":"Charlotte Solar & Roofing","applied":"2026-02-27","description":"8.6kW roof-mount solar PV system w/ 21 panels"},{"id":"BP-48C13D05","address":"29749 Pan American Blvd, North Port, FL","city":"North Port","status":"Final","lat":27.076575,"lng":-82.182373,"contractor":"Trinity Solar FL","applied":"2026-04-22","description":"9.0kW roof-mount solar PV system w/ 22 panels"},{"id":"BP-0E4D904A","address":"21456 Tropicaire Blvd, North Port, FL","city":"North Port","status":"Pending","lat":26.989031,"lng":-82.292176,"contractor":"Titan Solar Power","applied":"2026-03-24","description":"4.7kW roof-mount solar PV system w/ 11 panels"}]};


// ════════════════════════════════════════════════════════════════════
// CITY ADAPTER SYSTEM (BACKEND-ANALOG)
// ────────────────────────────────────────────────────────────────────
// Each adapter is an async function(cityCfg) -> Promise<Permit[]>
// That returns NORMALIZED permit records:
//
//   {
//     id:         string,    // permit number
//     address:    string,
//     city:       string,
//     county:     string,
//     status:     'Pending'|'In Review'|'Issued'|'Final'|'On Hold',
//     lat:        number,
//     lng:        number,
//     contractor: string,
//     applied:    'YYYY-MM-DD',
//     description:string,
//   }
//
// Adding a new adapter type = drop a function in this section.
// Adding a new city          = add one entry to CITY_REGISTRY below.
// ════════════════════════════════════════════════════════════════════

/** EmbeddedAdapter: pulls from EMBEDDED_DATA (works offline) */
const EmbeddedAdapter = (cfg) => async () => {
  // Simulate light async to show loading state
  await new Promise(r => setTimeout(r, 300));
  const data = EMBEDDED_DATA[cfg.id];
  if (!data) throw new Error(`No embedded data for ${cfg.id}`);
  return normalizePermits(data, cfg);
};

/** StaticJsonAdapter: fetches permits-{cityId}.json from same directory.
 *  Use this when you generate JSON files server-side via the Python scraper. */
const StaticJsonAdapter = (cfg) => async () => {
  const url = cfg.dataUrl || `permits-${cfg.id}.json`;
  const r = await fetch(url, { cache: 'no-store' });
  if (!r.ok) throw new Error(`HTTP ${r.status} fetching ${url}`);
  const data = await r.json();
  // Accept either {permits: [...]} or raw array
  return normalizePermits(Array.isArray(data) ? data : data.permits || [], cfg);
};

/** ApiProxyAdapter: hits a backend endpoint that proxies the actual scraper.
 *  Future use — wire this up when a backend exists.
 *  Example: cfg.apiUrl = 'https://api.yourdomain.com/permits/{cityId}' */
const ApiProxyAdapter = (cfg) => async () => {
  const url = (cfg.apiUrl || '/api/permits/{city}').replace('{city}', cfg.id);
  const r = await fetch(url);
  if (!r.ok) throw new Error(`API returned ${r.status}`);
  const data = await r.json();
  return normalizePermits(data.permits || data, cfg);
};

/** HybridAdapter: tries the static JSON file first, falls back to embedded
 *  sample data if the file isn't present (404). This is what scraped cities
 *  use — once your daily GitHub Action runs, the JSON file appears and the
 *  app silently switches from sample to live data. */
const HybridAdapter = (cfg) => async () => {
  const url = cfg.dataUrl || `permits-${cfg.id}.json`;
  try {
    const r = await fetch(url, { cache: 'no-store' });
    if (r.ok) {
      const data = await r.json();
      const list = Array.isArray(data) ? data : (data.permits || []);
      if (list.length > 0) {
        return normalizePermits(list, cfg);
      }
    }
  } catch (e) {
    // network error or parse error — fall through to embedded
  }
  // Fall back to embedded sample data
  const sample = EMBEDDED_DATA[cfg.id];
  if (!sample) throw new Error(`No data available for ${cfg.id}`);
  return normalizePermits(sample, cfg);
};

/** Normalizes any incoming permit shape into our canonical schema.
 *  Forgiving: accepts permit_id / id / number, applied / applied_date / issued, etc. */
function normalizePermits(rawList, cfg) {
  return rawList.map(r => ({
    id:          r.id || r.permit_id || r.permit_number || r.number || '',
    address:     r.address || r.site_address || '',
    city:        r.city || cfg.name,
    county:      r.county || cfg.county || '',
    status:      normalizeStatus(r.status),
    lat:         Number(r.lat ?? r.latitude),
    lng:         Number(r.lng ?? r.longitude ?? r.lon),
    contractor:  r.contractor || r.applicant || r.business_name || '',
    applied:     normalizeDate(r.applied || r.applied_date || r.issued_date || r.date_issued),
    description: r.description || r.work_description || '',
  })).filter(p => p.id && !isNaN(p.lat) && !isNaN(p.lng));
}

function normalizeStatus(s) {
  if (!s) return 'Pending';
  const lo = String(s).toLowerCase();
  if (lo.includes('pending') || lo.includes('submitted') || lo.includes('applied')) return 'Pending';
  if (lo.includes('review') || lo.includes('plan check')) return 'In Review';
  if (lo.includes('issued') || lo.includes('approved') || lo.includes('active')) return 'Issued';
  if (lo.includes('final') || lo.includes('complete') || lo.includes('closed') || lo.includes('co')) return 'Final';
  if (lo.includes('hold') || lo.includes('rejected') || lo.includes('denied')) return 'On Hold';
  return s;
}

function normalizeDate(d) {
  if (!d) return '';
  // Accept YYYY-MM-DD, MM/DD/YYYY, ISO strings
  const s = String(d).trim();
  if (/^\d{4}-\d{2}-\d{2}/.test(s)) return s.slice(0, 10);
  const parsed = new Date(s);
  if (!isNaN(parsed)) return parsed.toISOString().slice(0, 10);
  return '';
}


// ════════════════════════════════════════════════════════════════════
// CITY REGISTRY (the scalable part)
// ────────────────────────────────────────────────────────────────────
// Adding a new Florida city = ONE entry below. That's it.
//
// Fields:
//   id        — url-safe slug
//   name      — display name
//   county    — county name
//   center    — [lat, lng] for default map view
//   tier      — 'free' | 'pro' (gates access for paywall)
//   adapter   — adapter factory function
//   source    — 'live' | 'cached' | 'beta' (badge in dropdown)
//   region    — group label in dropdown ('Southwest FL', etc.)
//
// To use real fetched JSON files instead of embedded data:
//   Change `adapter: EmbeddedAdapter` -> `adapter: StaticJsonAdapter`
//   Then drop a permits-{id}.json file next to this HTML.
// ════════════════════════════════════════════════════════════════════
const CITY_REGISTRY = [
  // ─── Free tier (HybridAdapter = JSON file if present, sample if not) ─
  // These three cities are scraped daily by scraper.py + GitHub Actions.
  // Once your workflow runs, permits-{cityId}.json appears next to this
  // HTML and the app automatically switches from sample to live data.
  { id:'port-charlotte',   name:'Port Charlotte',    county:'Charlotte',  region:'Southwest FL',
    center:[26.9989,-82.1006], adapter:HybridAdapter,   source:'live',  tier:'free' },
  { id:'north-port',       name:'North Port',        county:'Sarasota',   region:'Southwest FL',
    center:[27.0442,-82.2359], adapter:HybridAdapter,   source:'live',  tier:'free' },
  { id:'fort-myers',       name:'Fort Myers',        county:'Lee',        region:'Southwest FL',
    center:[26.6406,-81.8723], adapter:HybridAdapter,   source:'live',  tier:'free' },

  // ─── Free tier — embedded samples (not yet scraped) ──────────────────
  { id:'north-fort-myers', name:'North Fort Myers',  county:'Lee',        region:'Southwest FL',
    center:[26.6720,-81.8772], adapter:EmbeddedAdapter, source:'cached', tier:'free' },
  { id:'bonita-springs',   name:'Bonita Springs',    county:'Lee',        region:'Southwest FL',
    center:[26.3398,-81.7787], adapter:EmbeddedAdapter, source:'cached', tier:'free' },
  { id:'naples',           name:'Naples',            county:'Collier',    region:'Southwest FL',
    center:[26.1420,-81.7948], adapter:EmbeddedAdapter, source:'cached', tier:'free' },
  { id:'miami',            name:'Miami',             county:'Miami-Dade', region:'Southeast FL',
    center:[25.7617,-80.1918], adapter:EmbeddedAdapter, source:'beta',  tier:'free' },

  // ─── Pro tier preview entries (gated by paywall) ─────────────────
  // These show up in the dropdown but trigger the upgrade modal on click.
  // Easy to extend — just add more rows.
  { id:'orlando',          name:'Orlando',           county:'Orange',     region:'Central FL',
    center:[28.5383,-81.3792], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'tampa',            name:'Tampa',             county:'Hillsborough', region:'Tampa Bay',
    center:[27.9506,-82.4572], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'st-petersburg',    name:'St. Petersburg',    county:'Pinellas',   region:'Tampa Bay',
    center:[27.7676,-82.6403], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'jacksonville',     name:'Jacksonville',      county:'Duval',      region:'Northeast FL',
    center:[30.3322,-81.6557], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'fort-lauderdale',  name:'Fort Lauderdale',   county:'Broward',    region:'Southeast FL',
    center:[26.1224,-80.1373], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'west-palm-beach',  name:'West Palm Beach',   county:'Palm Beach', region:'Southeast FL',
    center:[26.7153,-80.0534], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'sarasota',         name:'Sarasota',          county:'Sarasota',   region:'Southwest FL',
    center:[27.3364,-82.5307], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
  { id:'cape-coral',       name:'Cape Coral',        county:'Lee',        region:'Southwest FL',
    center:[26.5629,-81.9495], adapter:EmbeddedAdapter, source:'live',  tier:'pro' },
];

const CITY_BY_ID = Object.fromEntries(CITY_REGISTRY.map(c => [c.id, c]));


// ════════════════════════════════════════════════════════════════════
// CACHE LAYER
// ────────────────────────────────────────────────────────────────────
// Avoids redundant fetches for the same city in the same session.
// 5-minute TTL — long enough to reduce calls, short enough to feel fresh.
// ════════════════════════════════════════════════════════════════════
const cache = new Map();  // cityId -> { permits, fetchedAt }
const CACHE_TTL_MS = 5 * 60 * 1000;

async function loadCityData(cityId, { forceRefresh = false } = {}) {
  const cfg = CITY_BY_ID[cityId];
  if (!cfg) throw new Error(`Unknown city: ${cityId}`);
  if (cfg.tier === 'pro' && !user.isPro) {
    showPaywall(cityId);
    throw new Error('PRO_REQUIRED');
  }

  const now = Date.now();
  const cached = cache.get(cityId);
  if (!forceRefresh && cached && (now - cached.fetchedAt) < CACHE_TTL_MS) {
    return cached.permits;
  }

  const adapter = cfg.adapter(cfg);
  const permits = await adapter();
  cache.set(cityId, { permits, fetchedAt: now });
  return permits;
}


// ════════════════════════════════════════════════════════════════════
// USER / PAYWALL STATE  (placeholder for real auth)
// ────────────────────────────────────────────────────────────────────
// In a future build, swap in real auth: Stripe, Auth0, Supabase, etc.
// ════════════════════════════════════════════════════════════════════
const user = {
  isPro: false,   // ← flip to true to unlock pro-tier cities for testing
  email: null,
};


// ════════════════════════════════════════════════════════════════════
// FRONTEND STATE
// ════════════════════════════════════════════════════════════════════
const state = {
  cityId: null,
  permits: [],
  filters: {
    status: 'all',
    contractor: '',
    dateFrom: '',
    dateTo: '',
    search: '',
  },
  view: 'map',
  sort: { col: 'applied', dir: 'desc' },
  selected: null,
};


// ════════════════════════════════════════════════════════════════════
// CITY DROPDOWN
// ════════════════════════════════════════════════════════════════════
function renderCityList() {
  const list = document.getElementById('city-list');
  const q = (document.getElementById('city-search').value || '').toLowerCase().trim();

  // Group by region
  const groups = {};
  for (const cfg of CITY_REGISTRY) {
    if (q && !cfg.name.toLowerCase().includes(q) && !cfg.county.toLowerCase().includes(q)) continue;
    const key = cfg.region;
    if (!groups[key]) groups[key] = [];
    groups[key].push(cfg);
  }

  if (Object.keys(groups).length === 0) {
    list.innerHTML = '<div style="padding:20px;text-align:center;color:var(--muted);font-size:12px">No cities match "' + escapeHtml(q) + '"</div>';
    return;
  }

  list.innerHTML = Object.entries(groups).map(([region, cities]) => `
    <div class="city-group-label">${escapeHtml(region)}</div>
    ${cities.map(c => {
      const isPro = c.tier === 'pro';
      const isActive = state.cityId === c.id;
      const badgeClass = c.source === 'live' ? 'live' : c.source === 'beta' ? 'beta' : '';
      const badgeText = isPro ? 'PRO' : c.source.toUpperCase();
      return `
        <div class="city-option ${isActive ? 'active' : ''}" onclick="selectCity('${c.id}')">
          <div>
            <div class="city-option-name">${escapeHtml(c.name)}</div>
            <div class="city-option-meta">${escapeHtml(c.county)} County</div>
          </div>
          <div class="badge ${badgeClass}">${badgeText}</div>
        </div>
      `;
    }).join('')}
  `).join('');
}

function toggleCityDropdown(e) {
  e.stopPropagation();
  const dd = document.getElementById('city-dropdown');
  const btn = document.getElementById('city-btn');
  const isOpen = dd.classList.toggle('open');
  btn.classList.toggle('open', isOpen);
  if (isOpen) {
    renderCityList();
    setTimeout(() => document.getElementById('city-search').focus(), 50);
  }
}

function filterCityList() { renderCityList(); }

function closeCityDropdown() {
  document.getElementById('city-dropdown').classList.remove('open');
  document.getElementById('city-btn').classList.remove('open');
}

document.addEventListener('click', e => {
  if (!e.target.closest('.city-picker')) closeCityDropdown();
});


// ════════════════════════════════════════════════════════════════════
// CITY SELECTION (the orchestrator)
// ════════════════════════════════════════════════════════════════════
async function selectCity(cityId) {
  closeCityDropdown();
  if (state.cityId === cityId && state.permits.length) return;

  const cfg = CITY_BY_ID[cityId];
  if (!cfg) return;

  // Pro gate
  if (cfg.tier === 'pro' && !user.isPro) {
    showPaywall(cityId);
    return;
  }

  state.cityId = cityId;
  state.permits = [];
  state.selected = null;
  closePopup();

  document.getElementById('city-btn-label').textContent = cfg.name;
  document.getElementById('city-btn-meta').textContent = cfg.county;

  showState('loading', `Fetching ${cfg.name} permits…`);

  try {
    const permits = await loadCityData(cityId);
    state.permits = permits;

    if (permits.length === 0) {
      showState('empty', `No solar permits found for ${cfg.name}.`);
      return;
    }

    hideStates();

    // Recenter map on city
    view.centerLat = cfg.center[0];
    view.centerLng = cfg.center[1];
    for (const img of visibleTiles.values()) img.remove();
    visibleTiles.clear();
    createPins();
    fitAll();
    render();

    showToast(`Loaded ${permits.length} permits for ${cfg.name}`, 'success');
  } catch (err) {
    if (err.message === 'PRO_REQUIRED') return;
    console.error(err);
    showState('error', err.message || 'Failed to load permits');
  }
}

async function refreshData() {
  if (!state.cityId) {
    showToast('Select a city first', 'error');
    return;
  }
  const btn = document.getElementById('refresh-btn');
  btn.classList.add('refreshing');
  btn.disabled = true;
  try {
    cache.delete(state.cityId);  // bust cache
    const permits = await loadCityData(state.cityId, { forceRefresh: true });
    state.permits = permits;
    createPins();
    render();
    showToast('Data refreshed', 'success');
  } catch (err) {
    showToast('Refresh failed: ' + err.message, 'error');
  } finally {
    btn.classList.remove('refreshing');
    btn.disabled = false;
  }
}


// ════════════════════════════════════════════════════════════════════
// STATE OVERLAYS
// ════════════════════════════════════════════════════════════════════
function showState(name, subtitle) {
  hideStates();
  const el = document.getElementById('state-' + name);
  if (!el) return;
  if (subtitle) {
    const sub = el.querySelector('.state-subtitle');
    if (sub) sub.textContent = subtitle;
  }
  el.classList.add('show');
}

function hideStates() {
  ['loading','empty','error','welcome'].forEach(n => {
    const el = document.getElementById('state-' + n);
    if (el) el.classList.remove('show');
  });
}


// ════════════════════════════════════════════════════════════════════
// FILTERS
// ════════════════════════════════════════════════════════════════════
function setStatusFilter(el) {
  document.querySelectorAll('#status-filters .chip').forEach(c => c.classList.remove('on'));
  el.classList.add('on');
  state.filters.status = el.dataset.status;
  render();
}

function getFiltered() {
  const f = state.filters;
  return state.permits.filter(p => {
    if (f.status !== 'all' && p.status !== f.status) return false;
    if (f.contractor && !((p.contractor||'').toLowerCase().includes(f.contractor.toLowerCase()))) return false;
    if (f.dateFrom && (p.applied || '') < f.dateFrom) return false;
    if (f.dateTo && (p.applied || '') > f.dateTo) return false;
    if (f.search) {
      const hay = (p.address+' '+(p.contractor||'')+' '+p.id+' '+(p.description||'')).toLowerCase();
      if (!hay.includes(f.search)) return false;
    }
    return true;
  });
}


// ════════════════════════════════════════════════════════════════════
// VIEW TOGGLE
// ════════════════════════════════════════════════════════════════════
function setView(viewName) {
  state.view = viewName;
  document.querySelectorAll('.view-btn').forEach(b => b.classList.toggle('on', b.dataset.view === viewName));
  document.getElementById('map-container').classList.toggle('active', viewName === 'map');
  document.getElementById('table-container').classList.toggle('active', viewName === 'table');
  if (viewName === 'map') {
    // Reflow tiles on view return
    setTimeout(() => { loadTiles(); repositionPins(); }, 50);
  } else {
    renderTable();
  }
}


// ════════════════════════════════════════════════════════════════════
// RENDERING
// ════════════════════════════════════════════════════════════════════
function render() {
  // Read filter inputs
  state.filters.search = (document.getElementById('search')?.value || '').toLowerCase();
  state.filters.contractor = document.getElementById('contractor-filter')?.value || '';
  state.filters.dateFrom = document.getElementById('date-from')?.value || '';
  state.filters.dateTo = document.getElementById('date-to')?.value || '';

  if (state.view === 'map') {
    repositionPins();
  } else {
    renderTable();
  }
  renderList();
}

function renderList() {
  const list = document.getElementById('permit-list');
  const visible = getFiltered();

  const order = { 'Pending':1, 'In Review':2, 'On Hold':3, 'Issued':4, 'Final':5 };
  visible.sort((a, b) => {
    const oa = order[a.status]||9, ob = order[b.status]||9;
    if (oa !== ob) return oa - ob;
    return (b.applied || '').localeCompare(a.applied || '');
  });

  if (!state.cityId) {
    list.innerHTML = '<div style="padding:30px 14px;text-align:center;color:var(--muted);font-size:11px">Select a city above</div>';
    return;
  }
  if (visible.length === 0) {
    list.innerHTML = '<div style="padding:30px 14px;text-align:center;color:var(--muted);font-size:11px">No permits match your filters</div>';
    return;
  }

  list.innerHTML = visible.map(p => `
    <div class="permit-card ${state.selected===p.id?'selected':''}" data-status="${p.status}" data-id="${p.id}">
      <div class="permit-addr">${escapeHtml(p.address.split(',')[0])}</div>
      <div class="permit-meta">
        <strong>${p.status}</strong> · ${escapeHtml(p.contractor) || '—'}
      </div>
    </div>
  `).join('');
  list.querySelectorAll('.permit-card').forEach(el => {
    el.addEventListener('click', () => selectPermit(el.dataset.id));
  });
}


// ════════════════════════════════════════════════════════════════════
// TABLE VIEW
// ════════════════════════════════════════════════════════════════════
function renderTable() {
  const visible = getFiltered();

  // Sort
  const { col, dir } = state.sort;
  visible.sort((a, b) => {
    let va = a[col] || '', vb = b[col] || '';
    if (typeof va === 'string') { va = va.toLowerCase(); vb = (vb+'').toLowerCase(); }
    if (va < vb) return dir === 'asc' ? -1 : 1;
    if (va > vb) return dir === 'asc' ? 1 : -1;
    return 0;
  });

  // Toolbar with stats
  const counts = { 'Pending':0,'In Review':0,'Issued':0,'Final':0,'On Hold':0 };
  visible.forEach(p => { if (counts[p.status] !== undefined) counts[p.status]++; });
  const cfg = CITY_BY_ID[state.cityId];
  document.getElementById('table-toolbar').innerHTML = `
    <div style="font-size:14px;font-weight:700">${cfg ? escapeHtml(cfg.name) : 'No city selected'}</div>
    <div style="color:var(--muted);font-size:12px">${visible.length} permits</div>
    <div style="margin-left:auto;display:flex;gap:14px">
      <div class="toolbar-stat"><span class="stat-dot" style="background:#F59E0B"></span>Pending: <strong>${counts['Pending']}</strong></div>
      <div class="toolbar-stat"><span class="stat-dot" style="background:#3B82F6"></span>Review: <strong>${counts['In Review']}</strong></div>
      <div class="toolbar-stat"><span class="stat-dot" style="background:#10B981"></span>Issued: <strong>${counts['Issued']}</strong></div>
    </div>
  `;

  // Sort indicators
  document.querySelectorAll('.permits-table th').forEach(th => {
    const arrow = th.querySelector('.sort-arrow');
    if (!arrow) return;
    arrow.textContent = th.dataset.sort === col ? (dir === 'asc' ? '▲' : '▼') : '';
  });

  const body = document.getElementById('table-body');
  if (visible.length === 0) {
    body.innerHTML = `<tr><td colspan="5" style="text-align:center;padding:40px;color:var(--muted)">${state.cityId ? 'No permits match your filters' : 'Select a city to begin'}</td></tr>`;
    return;
  }

  body.innerHTML = visible.map(p => `
    <tr class="${state.selected===p.id?'selected':''}" data-id="${p.id}">
      <td class="cell-permit">${escapeHtml(p.id)}</td>
      <td class="cell-address">
        ${escapeHtml(p.address.split(',')[0])}
        <div class="city-tag">${escapeHtml(p.city)}, FL</div>
      </td>
      <td class="cell-contractor">${escapeHtml(p.contractor) || '—'}</td>
      <td class="cell-date">${escapeHtml(p.applied) || '—'}</td>
      <td><span class="status-pill" data-status="${p.status}">${p.status}</span></td>
    </tr>
  `).join('');

  body.querySelectorAll('tr').forEach(tr => {
    tr.addEventListener('click', () => selectPermit(tr.dataset.id));
  });
}

// Table sort
document.addEventListener('DOMContentLoaded', () => {
  document.querySelectorAll('.permits-table th[data-sort]').forEach(th => {
    th.addEventListener('click', () => {
      const col = th.dataset.sort;
      if (state.sort.col === col) {
        state.sort.dir = state.sort.dir === 'asc' ? 'desc' : 'asc';
      } else {
        state.sort.col = col;
        state.sort.dir = 'asc';
      }
      renderTable();
    });
  });
});


// ════════════════════════════════════════════════════════════════════
// PAYWALL
// ════════════════════════════════════════════════════════════════════
function showPaywall(reason) {
  const titleEl = document.getElementById('paywall-title');
  const subEl = document.getElementById('paywall-sub');
  if (reason && reason !== 'all-cities') {
    const cfg = CITY_BY_ID[reason];
    if (cfg) {
      titleEl.textContent = `Unlock ${cfg.name}`;
      subEl.textContent = `${cfg.name}, ${cfg.county} County is a Pro-tier city. Upgrade for full access to all 411 Florida cities and live data feeds.`;
    }
  } else {
    titleEl.textContent = 'FloridaSolar Pro';
    subEl.textContent = 'Unlock the full Florida network and live data feeds.';
  }
  document.getElementById('paywall').classList.add('show');
}

function hidePaywall() {
  document.getElementById('paywall').classList.remove('show');
}

function handleUpgrade() {
  // PLACEHOLDER: integrate Stripe / Lemon Squeezy / Paddle here
  // For now, demo unlock so you can poke around
  user.isPro = true;
  hidePaywall();
  showToast('Pro unlocked (demo)', 'success');
  renderCityList();
}


// ════════════════════════════════════════════════════════════════════
// MAP (preserved from previous build)
// ════════════════════════════════════════════════════════════════════
const TILE_SIZE = 256;
const TILE_SERVERS = [
  'https://a.tile.openstreetmap.org',
  'https://b.tile.openstreetmap.org',
  'https://c.tile.openstreetmap.org',
];
let tileServerIdx = 0;

const view = { centerLat: 27.025, centerLng: -82.17, zoom: 12 };

let mapContainer, tileLayer, pinLayer;
let isDragging = false, dragStart = null;
let pinElements = {};
let activePopup = null;
const visibleTiles = new Map();

function lonToTileX(lon, z) { return ((lon + 180) / 360) * Math.pow(2, z); }
function latToTileY(lat, z) {
  const rad = lat * Math.PI / 180;
  return (1 - Math.log(Math.tan(rad) + 1 / Math.cos(rad)) / Math.PI) / 2 * Math.pow(2, z);
}
function tileXToLon(x, z) { return x / Math.pow(2, z) * 360 - 180; }
function tileYToLat(y, z) {
  const n = Math.PI - 2 * Math.PI * y / Math.pow(2, z);
  return 180 / Math.PI * Math.atan(0.5 * (Math.exp(n) - Math.exp(-n)));
}
function lngLatToScreen(lng, lat) {
  const w = mapContainer.clientWidth, h = mapContainer.clientHeight, z = view.zoom;
  const tx = lonToTileX(lng, z), ty = latToTileY(lat, z);
  const cx = lonToTileX(view.centerLng, z), cy = latToTileY(view.centerLat, z);
  return { x: (tx - cx) * TILE_SIZE + w/2, y: (ty - cy) * TILE_SIZE + h/2 };
}
function screenToLngLat(px, py) {
  const w = mapContainer.clientWidth, h = mapContainer.clientHeight, z = view.zoom;
  const cx = lonToTileX(view.centerLng, z), cy = latToTileY(view.centerLat, z);
  return { lng: tileXToLon(cx + (px - w/2)/TILE_SIZE, z), lat: tileYToLat(cy + (py - h/2)/TILE_SIZE, z) };
}

function loadTiles() {
  const w = mapContainer.clientWidth, h = mapContainer.clientHeight;
  const z = Math.round(view.zoom);
  const cx = lonToTileX(view.centerLng, z), cy = latToTileY(view.centerLat, z);
  const tilesAcross = Math.ceil(w / TILE_SIZE) + 2;
  const tilesDown = Math.ceil(h / TILE_SIZE) + 2;
  const sx = Math.floor(cx - tilesAcross/2), sy = Math.floor(cy - tilesDown/2);
  const ex = sx + tilesAcross, ey = sy + tilesDown;
  const needed = new Set();

  for (let x = sx; x <= ex; x++) {
    for (let y = sy; y <= ey; y++) {
      const wx = ((x % Math.pow(2, z)) + Math.pow(2, z)) % Math.pow(2, z);
      if (y < 0 || y >= Math.pow(2, z)) continue;
      const key = `${z}/${wx}/${y}`;
      needed.add(key);
      if (!visibleTiles.has(key)) {
        const img = document.createElement('img');
        img.className = 'map-tile';
        img.style.width = TILE_SIZE + 'px';
        img.style.height = TILE_SIZE + 'px';
        img.draggable = false;
        const server = TILE_SERVERS[tileServerIdx++ % TILE_SERVERS.length];
        img.src = `${server}/${z}/${wx}/${y}.png`;
        img.onerror = () => { img.style.opacity = '0'; };
        const px = (x - cx) * TILE_SIZE + w/2, py = (y - cy) * TILE_SIZE + h/2;
        img.style.left = px + 'px'; img.style.top = py + 'px';
        img.dataset.tileX = x; img.dataset.tileY = y;
        tileLayer.appendChild(img);
        visibleTiles.set(key, img);
      } else {
        const img = visibleTiles.get(key);
        const px = (x - cx) * TILE_SIZE + w/2, py = (y - cy) * TILE_SIZE + h/2;
        img.style.left = px + 'px'; img.style.top = py + 'px';
        img.dataset.tileX = x; img.dataset.tileY = y;
      }
    }
  }
  for (const [k, im] of visibleTiles.entries()) {
    if (!needed.has(k)) { im.remove(); visibleTiles.delete(k); }
  }
}

function repositionTiles() {
  const w = mapContainer.clientWidth, h = mapContainer.clientHeight;
  const z = Math.round(view.zoom);
  const cx = lonToTileX(view.centerLng, z), cy = latToTileY(view.centerLat, z);
  for (const img of visibleTiles.values()) {
    const tx = parseFloat(img.dataset.tileX), ty = parseFloat(img.dataset.tileY);
    img.style.left = (tx - cx) * TILE_SIZE + w/2 + 'px';
    img.style.top = (ty - cy) * TILE_SIZE + h/2 + 'px';
  }
}

function statusColor(s) {
  return ({'Pending':'#F59E0B','In Review':'#3B82F6','Issued':'#10B981','Final':'#6B7280','On Hold':'#EF4444'})[s] || '#7c8ba5';
}

function createPins() {
  pinLayer.innerHTML = '';
  pinElements = {};
  state.permits.forEach(p => {
    const pin = document.createElement('div');
    pin.className = 'map-pin';
    pin.dataset.id = p.id;
    const marker = document.createElement('div');
    marker.className = 'pin-marker' + (p.status === 'Pending' ? ' urgent' : '');
    marker.style.background = statusColor(p.status);
    marker.style.boxShadow = '0 0 8px ' + statusColor(p.status);
    const icon = document.createElement('div');
    icon.className = 'pin-icon'; icon.textContent = '☼';
    marker.appendChild(icon);
    pin.appendChild(marker);
    pin.addEventListener('click', e => { e.stopPropagation(); selectPermit(p.id); });
    pinLayer.appendChild(pin);
    pinElements[p.id] = pin;
  });
}

function repositionPins() {
  const visible = getFiltered();
  const visIds = new Set(visible.map(p => p.id));
  const w = mapContainer.clientWidth, h = mapContainer.clientHeight;
  state.permits.forEach(p => {
    const pin = pinElements[p.id];
    if (!pin) return;
    if (!visIds.has(p.id)) { pin.style.display = 'none'; return; }
    pin.style.display = 'block';
    const s = lngLatToScreen(p.lng, p.lat);
    if (s.x < -50 || s.x > w + 50 || s.y < -50 || s.y > h + 50) { pin.style.display = 'none'; return; }
    pin.style.left = s.x + 'px'; pin.style.top = s.y + 'px';
  });
  if (activePopup) {
    const p = state.permits.find(x => x.id === activePopup.dataset.permitId);
    if (p) {
      const s = lngLatToScreen(p.lng, p.lat);
      activePopup.style.left = s.x + 'px';
      activePopup.style.top = s.y + 'px';
    }
  }
}

function startDrag(e) {
  isDragging = true;
  dragStart = { x: e.clientX, y: e.clientY, centerLat: view.centerLat, centerLng: view.centerLng };
  if (mapContainer) mapContainer.style.cursor = 'grabbing';
}
function onDrag(e) {
  if (!isDragging || !dragStart) return;
  const z = view.zoom;
  const dx = e.clientX - dragStart.x, dy = e.clientY - dragStart.y;
  const sx = lonToTileX(dragStart.centerLng, z), sy = latToTileY(dragStart.centerLat, z);
  view.centerLng = tileXToLon(sx - dx/TILE_SIZE, z);
  view.centerLat = tileYToLat(sy - dy/TILE_SIZE, z);
  repositionTiles(); repositionPins();
}
function endDrag() {
  if (isDragging) { isDragging = false; dragStart = null; if (mapContainer) mapContainer.style.cursor = 'grab'; loadTiles(); }
}
function onWheel(e) {
  e.preventDefault();
  const r = mapContainer.getBoundingClientRect();
  zoomToward(e.deltaY > 0 ? -1 : 1, e.clientX - r.left, e.clientY - r.top);
}
function zoomToward(d, ax, ay) {
  const z = Math.max(8, Math.min(18, Math.round(view.zoom + d)));
  if (z === view.zoom) return;
  const before = screenToLngLat(ax || mapContainer.clientWidth/2, ay || mapContainer.clientHeight/2);
  view.zoom = z;
  for (const img of visibleTiles.values()) img.remove();
  visibleTiles.clear();
  const after = screenToLngLat(ax || mapContainer.clientWidth/2, ay || mapContainer.clientHeight/2);
  view.centerLng += (before.lng - after.lng);
  view.centerLat += (before.lat - after.lat);
  loadTiles(); repositionPins();
}
function zoomIn() { zoomToward(1); }
function zoomOut() { zoomToward(-1); }

function fitAll() {
  const visible = getFiltered();
  if (visible.length === 0) return;
  const lats = visible.map(p => p.lat), lngs = visible.map(p => p.lng);
  const minLat = Math.min(...lats), maxLat = Math.max(...lats);
  const minLng = Math.min(...lngs), maxLng = Math.max(...lngs);
  view.centerLat = (minLat + maxLat) / 2;
  view.centerLng = (minLng + maxLng) / 2;
  const w = mapContainer.clientWidth, h = mapContainer.clientHeight;
  let bestZ = 8;
  for (let z = 18; z >= 8; z--) {
    const minTX = lonToTileX(minLng, z), maxTX = lonToTileX(maxLng, z);
    const minTY = latToTileY(maxLat, z), maxTY = latToTileY(minLat, z);
    if ((maxTX - minTX) * TILE_SIZE + 80 <= w && (maxTY - minTY) * TILE_SIZE + 80 <= h) { bestZ = z; break; }
  }
  view.zoom = bestZ;
  for (const img of visibleTiles.values()) img.remove();
  visibleTiles.clear();
  loadTiles(); repositionPins();
}

function selectPermit(id) {
  const p = state.permits.find(x => x.id === id);
  if (!p) return;
  state.selected = id;
  if (state.view === 'map') {
    view.centerLat = p.lat; view.centerLng = p.lng;
    if (view.zoom < 14) {
      view.zoom = 15;
      for (const img of visibleTiles.values()) img.remove();
      visibleTiles.clear();
    }
    loadTiles(); repositionTiles(); repositionPins();
    showPopup(p);
    Object.entries(pinElements).forEach(([pid, el]) => el.classList.toggle('selected', pid === id));
  }
  document.querySelectorAll('.permit-card').forEach(c => c.classList.toggle('selected', c.dataset.id === id));
  document.querySelectorAll('#table-body tr').forEach(tr => tr.classList.toggle('selected', tr.dataset.id === id));
}

function showPopup(p) {
  closePopup();
  const popup = document.createElement('div');
  popup.className = 'popup';
  popup.dataset.permitId = p.id;
  popup.innerHTML = `
    <button class="popup-close" onclick="closePopup()">×</button>
    <div class="popup-title">${escapeHtml(p.address.split(',')[0])}</div>
    <div class="popup-status" data-status="${p.status}">${p.status}</div>
    <div class="popup-meta">
      <strong>${escapeHtml(p.id)}</strong><br>
      ${p.contractor ? 'Contractor: ' + escapeHtml(p.contractor) + '<br>' : ''}
      ${p.applied ? 'Applied: ' + escapeHtml(p.applied) + '<br>' : ''}
      ${p.description ? escapeHtml(p.description) : ''}
    </div>
  `;
  const s = lngLatToScreen(p.lng, p.lat);
  popup.style.left = s.x + 'px'; popup.style.top = s.y + 'px';
  popup.style.pointerEvents = 'auto';
  pinLayer.appendChild(popup);
  activePopup = popup;
}
function closePopup() {
  if (activePopup) { activePopup.remove(); activePopup = null; }
}


// ════════════════════════════════════════════════════════════════════
// UTILS
// ════════════════════════════════════════════════════════════════════
function escapeHtml(s) {
  if (s == null) return '';
  return String(s)
    .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;').replace(/'/g, '&#039;');
}

function showToast(msg, type) {
  const t = document.getElementById('toast');
  t.textContent = msg;
  t.className = 'toast show ' + (type || '');
  setTimeout(() => t.classList.remove('show'), 2800);
}


// ════════════════════════════════════════════════════════════════════
// BOOT
// ════════════════════════════════════════════════════════════════════
window.addEventListener('load', () => {
  mapContainer = document.getElementById('map-container');
  tileLayer = document.getElementById('tile-layer');
  pinLayer = document.getElementById('pin-layer');

  // Map events
  mapContainer.addEventListener('mousedown', startDrag);
  window.addEventListener('mousemove', onDrag);
  window.addEventListener('mouseup', endDrag);
  mapContainer.addEventListener('wheel', onWheel, { passive: false });
  mapContainer.addEventListener('touchstart', e => {
    if (e.touches.length === 1) startDrag({ clientX: e.touches[0].clientX, clientY: e.touches[0].clientY });
  }, { passive: true });
  mapContainer.addEventListener('touchmove', e => {
    if (e.touches.length === 1 && isDragging) {
      e.preventDefault();
      onDrag({ clientX: e.touches[0].clientX, clientY: e.touches[0].clientY });
    }
  }, { passive: false });
  mapContainer.addEventListener('touchend', endDrag);
  mapContainer.addEventListener('click', e => {
    if (e.target === mapContainer || e.target === tileLayer || e.target.classList.contains('map-tile')) {
      closePopup();
    }
  });
  window.addEventListener('resize', () => { loadTiles(); repositionTiles(); repositionPins(); });

  // Search debounce
  let searchTimer;
  document.getElementById('search').addEventListener('input', () => {
    clearTimeout(searchTimer);
    searchTimer = setTimeout(render, 150);
  });

  // Modal close on overlay click
  document.getElementById('paywall').addEventListener('click', e => {
    if (e.target.id === 'paywall') hidePaywall();
  });

  // Initial state: welcome
  showState('welcome');

  // Initialize tile layer (it'll fully load once a city is selected)
  loadTiles();
});
</script>

</body>
</html>
