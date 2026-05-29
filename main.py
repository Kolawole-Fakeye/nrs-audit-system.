from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd
import time
import os

app = FastAPI(
    title="NRS: Automated Data Audit API",
    description="Programmatic anomaly detection and schema normalization engine for fiscal compliance logs.",
    version="2.0.0"
)

# Enable CORS so your Streamlit frontend can communicate with this API securely in the cloud
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Global constant to track application boot time for synthetic uptime checks
START_TIME = time.time()
DATA_FILE = "nrs_audited_results.parquet"

def ensure_mock_data_exists():
    """
    Data Layer Safeguard (Optimized for Parquet Clean Build).
    If the binary file is missing, this generates your clean compliance
    dataset using Apache Parquet for high-performance columnar data loading.
    """
    if not os.path.exists(DATA_FILE):
        mock_data = {
            "Tax_Paid": [2500000, 750000, 12000000, 450000, 8500000],
            "Sector": ["Oil & Gas", "Retail", "Telecommunications", "Agriculture", "Banking"],
            "Region": ["Lagos", "Kano", "Abuja", "Ibadan", "Port Harcourt"],
            "Is_Anomaly": ["False", "True", "False", "False", "True"]
        }
        df = pd.DataFrame(mock_data)
        # Using pyarrow engine to save as an optimized binary file
        df.to_parquet(DATA_FILE, engine="pyarrow", index=False)
        print("Clean Build Status: High-performance Parquet cache generated successfully.")

# Ensure data asset integrity on server startup
ensure_mock_data_exists()

@app.get("/", tags=["General"])
def home():
    """
    Root endpoint confirming API availability with developer credentials.
    """
    return {
        "Status": "NRS API is Online", 
        "Engineer": "Kolawole Fakeye",
        "Role": "Systems & Automation Specialist",
        "Engine": "FastAPI + Parquet Core Pipeline"
    }

@app.get("/health", tags=["Observability"])
async def health_check():
    """
    Synthetic Monitoring & Health Endpoint.
    Verifies Parquet file availability and calculates system uptime telemetry.
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
            "storage_format": "Apache Parquet (Columnar)",
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
    Retrieves compliance logs from the high-performance Parquet storage layer.
    """
    try:
        ensure_mock_data_exists()
        # Read directly from the optimized binary format
        df = pd.read_parquet(DATA_FILE, engine="pyarrow")
        
        # Enforce column standardization dynamically to prevent structural drift crashes
        df.columns = [c.replace(' ', '_').strip() for c in df.columns]
            
        return df.to_dict(orient="records")
        
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Data Processing Error: {str(e)}"
        )
