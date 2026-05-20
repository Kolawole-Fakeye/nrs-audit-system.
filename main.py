from fastapi import FastAPI
import pandas as pd

app = FastAPI()

@app.get("/")
def home():
    return {"Status": "NRS API is Online", "Engineer": "Kolawole"}

@app.get("/data")
def get_data():
    df = pd.read_csv("nrs_audited_results.csv")
    # This line ensures the column is named correctly even if the CSV changed
    if 'Is_Anomaly' not in df.columns:
        # If it's lowercase or has a space, this fixes it
        df.columns = [c.replace(' ', '_').title() for c in df.columns]
    return df.to_dict(orient="records")