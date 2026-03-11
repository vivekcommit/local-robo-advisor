FAKE_HOLDINGS = [
    {"symbol": "VTI", "quantity": 10, "price": 250.0},
    {"symbol": "VXUS", "quantity": 15, "price": 60.0},
    {"symbol": "BND", "quantity": 20, "price": 75.0},
]

def compute_total_value():
    return sum(h["quantity"] * h["price"] for h in FAKE_HOLDINGS)

def get_dashboard_snapshot():
    total_value = compute_total_value()
    return {
        "total_value": total_value,
        "holdings": FAKE_HOLDINGS,
    }

def get_all_holdings():
    return FAKE_HOLDINGS
