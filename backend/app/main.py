from fastapi import FastAPI
from .services.portfolio import get_dashboard_snapshot, get_all_holdings

app = FastAPI(title="Local Robo Advisor")

@app.get("/api/dashboard")
def read_dashboard():
    snapshot = get_dashboard_snapshot()
    return {
        "message": "Local robo-advisor is running",
        **snapshot,
    }

@app.get("/api/holdings")
def read_holdings():
    return get_all_holdings()
