from fastapi import FastAPI, HTTPException
from contextlib import asynccontextmanager
from pydantic import BaseModel, Field
from typing import Optional
from .db import init_db 
from .services.portfolio import get_dashboard_snapshot, get_all_holdings, add_holding, update_holding, delete_holding

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup
    init_db()
    #seed_example_holding()
    yield
    # Shutdown (nothing yet, but we can add later)
    # e.g., close background tasks, etc.


app = FastAPI(lifespan=lifespan,title="Local Robo Advisor", description="A simple local robo-advisor API built with FastAPI and SQLite", version="1.0.0")

class HoldingIn(BaseModel):
    symbol: str = Field(min_length=1, example="VTI")
    quantity: float = Field(gt=0, example=10.0)
    price: float = Field(gt=0, example=250.0)
    cost_basis: float = Field(gt=0, example=220.0)

class HoldingUpdate(BaseModel):
    quantity: Optional[float] = Field(gt=0, example=10.0)
    price: Optional[float] = Field(gt=0, example=250.0)
    cost_basis: Optional[float] = Field(gt=0, example=220.0)

@app.post("/api/holdings")
def create_holding(holding: HoldingIn):
    add_holding(
        symbol=holding.symbol.upper(),
        quantity=holding.quantity,
        price=holding.price,
        cost_basis=holding.cost_basis
    )
    return {"message": "Holding added successfully"}

@app.put("/api/holdings/{holding_id}")
def update_holding_endpoint(holding_id: int, holding: HoldingUpdate):
    success = update_holding(
        holding_id=holding_id,
        quantity=holding.quantity,
        price=holding.price,
        cost_basis=holding.cost_basis
    )
    if not success:
        raise HTTPException(status_code=404, detail="Holding not found")
    return {"message": "Holding updated successfully"}

@app.delete("/api/holdings/{holding_id}")
def delete_holding_endpoint(holding_id: int):
    success = delete_holding(holding_id=holding_id)
    if not success:
        raise HTTPException(status_code=404, detail="Holding not found")
    return {"message": "Holding deleted successfully"}

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
