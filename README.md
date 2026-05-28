# NRS: Automated Data Audit API & Observability Pipeline

> **A programmatic data auditing engine designed to replace manual spreadsheet workflows with automated fiscal compliance monitoring, schema standardization, and synthetic health logging.**

---

## 📊 Live Interactive Dashboard
Recruiters and data professionals can interact with the live analytical frontend built for this pipeline:

👉 [**Launch the Live Streamlit Compliance Dashboard**](YOUR_STREAMLIT_COMMUNITY_CLOUD_URL_HERE)

*(Note: If the app is sleeping, please click "Wake up app" to spin up the containerized instance.)*

---

## 🛠️ Architecture & Core Features

This project bridges **Systems Engineering** with **Modern Data Automation** by deploying an observable data pipeline that ingests, cleans, and monitors compliance logs:

* **Automated Data Normalization:** Implements defensive programming via `pandas` to dynamically clean, format, and normalize compliance schemas at runtime, catching structural drift (e.g., lowercase conversion or whitespace anomalies) automatically.
* **Synthetic Monitoring & Observability:** Features a dedicated `/health` endpoint built alongside standard operational routes. This allows synthetic ping tools (like AWS Synthetic Canaries or custom Python cron scripts) to track API uptime metrics and verify system file dependencies proactively.
* **Production-Grade Error Handling:** Replaces fragile scripts with explicit HTTP status reporting (404/500 blocks), ensuring data corruption or environment-level asset drops are logged without crashing the active server daemon.

```text
                  [ FISCAL LOG DATA SOURCE ]
                              │
                              ▼
        [ FastAPI Backend Engine ] ──► [/health] ──► [ Synthetic Monitor ]
                              │
                              ▼
       [ Pandas Anomaly Detection & Normalization ]
                              │
                              ▼
    [ Streamlit Interactive UI / Recruiter View ]
