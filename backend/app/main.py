from fastapi import FastAPI
from contextlib import asynccontextmanager
from .db import init_db 
from .services.portfolio import get_dashboard_snapshot, get_all_holdings

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    #seed_example_holding()
    yield
    # Shutdown (nothing yet, but we can add later)
    # e.g., close background tasks, etc.


app = FastAPI(lifespan=lifespan,title="Local Robo Advisor", description="A simple local robo-advisor API built with FastAPI and SQLite", version="1.0.0")

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
