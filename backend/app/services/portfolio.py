from typing import List, Dict, Any

from ..db import get_connection

def add_holding(symbol: str, quantity: float, price: float, cost_basis: float, asset_class: str) -> None:
    conn = get_connection()
    try:
        conn.execute(
            """
            INSERT INTO holdings (symbol, quantity, price, cost_basis,asset_class)
            VALUES (?, ?, ?, ?, ?)
            """,
            (symbol.upper(), quantity, price, cost_basis, asset_class),
        )
        conn.commit()
    finally:
        conn.close()

def update_holding(holding_id: int, quantity: float, price: float, cost_basis: float, asset_class: str) -> bool:
    conn = get_connection()
    try:
        cursor=conn.execute(
            """
            UPDATE holdings
            SET quantity = ?, price = ?, cost_basis = ?, asset_class = ?
            WHERE id = ?
            """,
            (quantity, price, cost_basis, holding_id, asset_class),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

def delete_holding(holding_id: int) -> bool:
    conn = get_connection()
    try:
        cursor=conn.execute(
            """
            DELETE FROM holdings
            WHERE id = ?
            """,
            (holding_id,),
        )
        conn.commit()
        return cursor.rowcount > 0
    finally:
        conn.close()

def get_all_holdings() -> List[Dict[str, Any]]:
    conn = get_connection()
    try:
        rows = conn.execute(
            """
            SELECT id,symbol, quantity, price, cost_basis, asset_class
            FROM holdings
            ORDER BY symbol
            """
        ).fetchall()

        holdings: List[Dict[str, Any]] = []
        for row in rows:
            quantity = row["quantity"]
            price = row["price"]
            cost_basis = row["cost_basis"]

            current_value = quantity * price
            total_cost = quantity * cost_basis
            unrealized_gain_loss = current_value - total_cost

            holdings.append(
                {
                "id": row["id"],
                "symbol": row["symbol"],
                "quantity": row["quantity"],
                "price": row["price"],
                "cost_basis": row["cost_basis"],
                "asset_class": row["asset_class"],
                "unrealized_gain_loss": unrealized_gain_loss
            }
        )
        return holdings
    finally:
        conn.close()


def compute_total_value(holdings: List[Dict[str, Any]]) -> float:
    return sum(h["quantity"] * h["price"] for h in holdings)

def compute_total_cost(holdings: List[Dict[str, Any]]) -> float:
    return sum(h["quantity"] * h["cost_basis"] for h in holdings)

def compute_total_unrealized_gain_loss(holdings: List[Dict[str, Any]]) -> float:
    return sum(h["unrealized_gain_loss"] for h in holdings)

def get_dashboard_snapshot() -> Dict[str, Any]:
    holdings = get_all_holdings()
    total_value = compute_total_value(holdings)
    total_cost = compute_total_cost(holdings)
    total_unrealized_gain_loss = compute_total_unrealized_gain_loss(holdings)

    return {
        "summary": {
        "total_value": total_value,
        "total_cost": total_cost,
        "total_unrealized_gain_loss": total_unrealized_gain_loss,
        "positions_count": len(holdings),
        },
        "holdings": holdings,
    }