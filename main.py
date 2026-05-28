from fastapi import FastAPI, HTTPException
import pandas as pd
import time
import os

app = FastAPI(
    title="NRS: Automated Data Audit API",
    description="Programmatic anomaly detection and schema normalization engine for fiscal compliance logs.",
    version="1.0.0"
)

# Global constant to track application boot time for synthetic uptime checks
START_TIME = time.time()
DATA_FILE = "nrs_audited_results.csv"

def ensure_mock_data_exists():
    """
    Data Layer Safeguard.
    If the CSV file is missing, this automatically generates a clean compliance 
    dataset so the API and frontend never throw a 404/500 FileNotFoundError.
    """
    if not os.path.exists(DATA_FILE):
        mock_data = {
            "Tax_Paid": [2500000, 750000, 12000000, 450000, 8500000],
            "Sector": ["Oil & Gas", "Retail", "Telecommunications", "Agriculture", "Banking"],
            "Region": ["Lagos", "Kano", "Abuja", "Ibadan", "Port Harcourt"],
            "Is_Anomaly": ["False", "True", "False", "False", "True"]
        }
        df = pd.DataFrame(mock_data)
        df.to_csv(DATA_FILE, index=False)

# Ensure data asset integrity on server startup
ensure_mock_data_exists()

@app.get("/", tags=["General"])
def home():
    """
    Root endpoint confirming API availability.
    """
    return {
        "Status": "NRS API is Online", 
        "Engineer": "Kolawole Fakeye",
        "Role": "Systems & Automation Specialist"
    }

@app.get("/health", tags=["Observability"])
async def health_check():
    """
    Synthetic Monitoring & Health Endpoint.
    Verifies data file availability and calculates system uptime telemetry.
    """
    try:
        if not os.path.exists(DATA_FILE):
            raise FileNotFoundError(f"Critical data layer asset missing: {DATA_FILE}")
            
        uptime_seconds = time.time() - START_TIME
        
        return {
            "status": "healthy",
            "timestamp": time.time(),
            "uptime_hours": round(uptime_seconds / 3600, 4),
            "data_layer": "connected",
            "monitoring_type": "Synthetic Network Target"
        }
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"NRS Pipeline Unhealthy: {str(e)}"
        )

@app.get("/data", tags=["Data Retrieval"])
def get_data():
    """
    Retrieves compliance logs and enforces runtime schema standardization.
    """
    try:
        ensure_mock_data_exists()
        df = pd.read_csv(DATA_FILE)
        
        # Enforce column standardization dynamically to prevent structural drift crashes
        if 'Is_Anomaly' not in df.columns:
            df.columns = [c.replace(' ', '_').title() for c in df.columns]
            
        return df.to_dict(orient="records")
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Data Processing Error: {str(e)}"
        )
