from typing import List, Dict, Any

from ..db import get_connection


def get_all_holdings() -> List[Dict[str, Any]]:
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT symbol, quantity, price, cost_basis
            FROM holdings
            ORDER BY symbol
            """
        ).fetchall()
        return [
            {
                "symbol": row["symbol"],
                "quantity": row["quantity"],
                "price": row["price"],
                "cost_basis": row["cost_basis"],
            }
            for row in rows
        ]
    finally:
        conn.close()


def compute_total_value(holdings: List[Dict[str, Any]]) -> float:
    return sum(h["quantity"] * h["price"] for h in holdings)


def get_dashboard_snapshot() -> Dict[str, Any]:
    holdings = get_all_holdings()
    total_value = compute_total_value(holdings)

    return {
        "total_value": total_value,
        "holdings": holdings,
    }