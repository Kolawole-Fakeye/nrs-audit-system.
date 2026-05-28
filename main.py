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
    Verifies data file availability and calculates system uptime.
    """
    try:
        # Check if the target data file exists to confirm engine readiness
        file_target = "nrs_audited_results.csv"
        file_accessible = os.path.exists(file_target)
        
        if not file_accessible:
            raise FileNotFoundError(f"Critical data layer asset missing: {file_target}")
            
        uptime_seconds = time.time() - START_TIME
        
        return {
            "status": "healthy",
            "timestamp": time.time(),
            "uptime_hours": round(uptime_seconds / 3600, 4),
            "data_layer": "connected",
            "monitoring_type": "Synthetic Network Target"
        }
    except Exception as e:
        # Returns a 500 status code which immediately triggers an infrastructure monitoring alert
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
        df = pd.read_csv("nrs_audited_results.csv")
        
        # Enforce column standardization dynamically
        if 'Is_Anomaly' not in df.columns:
            df.columns = [c.replace(' ', '_').title() for c in df.columns]
            
        return df.to_dict(orient="records")
        
    except FileNotFoundError:
        raise HTTPException(
            status_code=404, 
            detail="Audited records data source file not found on the server."
        )
    except Exception as e:
        raise HTTPException(
            status_code=500, 
            detail=f"Internal Data Processing Error: {str(e)}"
        )
