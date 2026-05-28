NRS Automated Audit Pipeline
An enterprise-grade, cloud-deployed data processing and visualization pipeline built to automate the auditing processes of the Federal Inland Revenue Service (FIRS) / Nigeria Revenue Service (NRS).

The system leverages a decoupled architecture: an optimized FastAPI backend handles heavy data ingestion, validation, and normalization, while a reactive Streamlit frontend serves as an interactive compliance dashboard for senior leadership.

🔗 Live Deployments
🚀 Live Interactive Dashboard: https://nrs-automated-audit-pipeline-zjz3bim9bunmg4ncwv5zhn.streamlit.app/

⚙️ Production Backend API: [https://nrs-backend-api.onrender.com/docs](https://nrs-backend-api.onrender.com/docs)

🏗️ Architecture Overview
The pipeline is split into two independent cloud-hosted layers to ensure scalability and high availability:

Frontend Dashboard (Streamlit Cloud): Consumes normalized JSON payloads from the API and translates them into actionable financial metrics, compliance tracking tables, and data visualizations. Includes built-in CSV fallback handling.

Backend API (Render - Dockerized): Built with FastAPI and containerized via Docker. Manages schema validation, sanitizes column drift from incoming tax records, and exposes structured REST endpoints.

🛠️ Tech Stack
Frontend: Streamlit, Pandas, Plotly

Backend: Python, FastAPI, Uvicorn, Docker

Deployment & DevOps: GitHub, Render (Docker Runtime), Streamlit Community Cloud

🚀 Local Setup & Installation
To run this project locally, clone the repository and set up both components:

1. Prerequisites
Ensure you have Python 3.10+ and Docker installed.

2. Backend Setup
Bash


# Navigate to the project root
cd nrs-automated-audit-pipeline

# Install backend dependencies
pip install -r requirements.txt

# Start the FastAPI development server
uvicorn main:app --reload --port 8000
Access the local API documentation at: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

3. Frontend Setup
Open a new terminal window:

Bash


# Run the Streamlit interface
streamlit run app.py
Access the local UI at: http://localhost:8501

🔒 Environment & Configuration
For production deployment, configure your Streamlit Cloud provider environment variables or secrets with the following key:

Ini, TOML


NRS_BACKEND_URL = "https://nrs-backend-api.onrender.com/data"
📈 Core Capabilities Demonstrated
Containerization: Production deployment utilizing optimized Docker configurations.

Schema Drift Resilience: Ingestion algorithms capable of sanitizing and normalizing unstructured file schemas on the fly.

Decoupled Architecture: Clean separation of concerns between raw analytical processing (API) and presentation layers (UI).

Fault Tolerance: Robust exception mapping to guarantee uninterrupted dashboard operation even during network latency.
