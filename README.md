# ai-data-center
AI-powered data center monitoring with automated anomaly detection.


# AI Data Center Monitoring Dashboard

A lightweight, full-stack monitoring dashboard that simulates real-time server metrics (CPU, memory, disk usage) for a fictional data center, detects anomalies, and displays them on a live web dashboard.

This project was an early exploration of the same core problem I later solved at production scale with **PodSight**: ingest metrics, detect anomalies, and surface them through a usable interface.

## What it does

- Simulates live server metrics (CPU, memory, disk) for multiple servers
- Detects threshold-based anomalies (high CPU, high memory, high disk usage) and logs them
- Serves current metrics through a Flask API
- Displays metrics on a simple auto-refreshing web dashboard
- Includes a standalone Go version of the metrics loader (early exploration of a Go-based rewrite)

## Project structure

```
ai-data-center/
├── configs/
│   └── sample_metrics.json      # Seed data for server metrics (CPU/memory/disk %)
├── logs/
│   └── monitoring_alerts.csv    # Logged anomaly alerts (timestamp, server, metric, value, alert type)
├── scripts/
│   ├── go_version/               # Go implementation of the metrics loader
│   └── monitor.py                # Python monitoring loop: simulates data, detects anomalies, logs alerts
└── web/
    ├── app.py                    # Flask API serving live metrics at /metrics
    ├── index.html                 # Dashboard page
    ├── script.js                  # Fetches metrics from the API every 3s and renders them
    └── style.css                  # Dashboard styling
```

## How it works

1. **`monitor.py`** loads server metrics from `configs/sample_metrics.json`, randomly adjusts values each cycle to simulate real-time change, and checks each server against fixed thresholds:
   - CPU usage > 85% → High CPU Usage alert
   - Memory usage > 90% → High Memory Usage alert
   - Disk usage > 80% → High Disk Usage alert

   Alerts are logged to both a log file and `logs/monitoring_alerts.csv`.

2. **`app.py`** is a small Flask API that reads the current metrics file and exposes it at a `/metrics` GET endpoint, with CORS enabled for browser access.

3. **`script.js`** polls the `/metrics` endpoint every 3 seconds and renders each server's CPU, memory, and disk usage into the dashboard.

4. **`scripts/go_version/`** contains an early Go implementation that loads and parses the same metrics JSON — a first step toward a Go-based rewrite of the monitoring logic.

## Running it locally

**Backend (Flask API):**
```bash
cd web
pip install flask flask-cors
python app.py
```
This starts the API at `http://localhost:5000/metrics`.

> Note: `app.py` currently points to a hardcoded config path (`/workspaces/ai-data-center/configs/sample_metrics.json`). Update this to a relative path or environment variable before running outside the original dev container.

**Frontend (dashboard):**
Open `web/index.html` in a browser, or serve the `web/` directory with any static file server.

> Note: `script.js` currently points to a Codespaces-generated URL rather than `localhost:5000`. Update the `fetch()` URL in `script.js` to match wherever the Flask API is actually running.

**Monitoring loop (anomaly simulation):**
```bash
cd scripts
python monitor.py
```
Runs 5 simulated monitoring cycles, updating metrics and logging any threshold breaches.

## Known issues / to fix

- [ ] `app.py` uses a hardcoded absolute file path — breaks outside the original Codespaces environment
- [ ] `script.js` fetches from a stale Codespaces URL instead of a configurable/local endpoint
- [ ] No persistent database — metrics reset to the seed file on every load rather than tracking real history
- [ ] `monitor.py` and `app.py` don't share a live feedback loop — the dashboard reads the static config file, not the values `monitor.py` is actively simulating
- [ ] Go version (`scripts/go_version/`) only loads and prints metrics — no API or dashboard integration yet

## Possible next steps

- Fix the hardcoded paths/URLs so it runs consistently outside of Codespaces
- Connect `monitor.py`'s simulated updates to the same data source the API/dashboard reads from, so the dashboard reflects live simulated changes rather than the static seed file
- Replace the flat JSON file with a real database (e.g. MongoDB, matching the approach used in PodSight) to support historical tracking and trend charts
- Deploy the API and dashboard to AWS (e.g. Lambda + API Gateway for the backend, S3/CloudFront for the frontend) as a hands-on cloud deployment exercise
- Extend the anomaly model beyond fixed thresholds (e.g. rolling averages, rate-of-change detection) — similar to the counter vs. gauge metric handling used in PodSight

## Tech stack

- **Backend:** Python (Flask), Go (early prototype)
- **Frontend:** Vanilla HTML/CSS/JavaScript
- **Data:** JSON (seed data), CSV (alert logs)
