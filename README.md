# nrs-audit-system.# Nigeria Revenue Service (NRS) Automated Audit Pipeline

An automated data auditing and compliance API engineered to programmatically ingest, normalize, and expose verified financial transaction logs. Built using **FastAPI** and **Pandas**, this system replaces manual spreadsheet workflows with an automated runtime engine designed to detect anomalies, reconcile data schemas, and stream audit-ready data.

---

## 🚀 Key Architectural Features

* **High-Performance REST Node:** Implements an active backend engine using FastAPI to securely stream compliance data to operational analytics dashboards.
* **Self-Healing Schema Normalization:** Dynamically intercepts the data ingestion pipeline to correct formatting issues (e.g., spaces or inconsistent casing) on the fly, preventing downstream pipeline breakage.
* **Programmatic Flagging Matrix:** Validates structured corporate filing ledgers against targeted compliance data criteria to isolate entries marked with an administrative audit flag (`Is_Anomaly`).

---

## ⚙️ Core Architecture

The pipeline acts as a bridge between structured local transactional storage and cloud data layers:
