from typing import List, Dict, Any

from ..db import get_connection

def add_holding(symbol: str, quantity: float, price: float, cost_basis: float) -> None:
    conn = get_connection()
    try:
        conn.execute(
            """
            INSERT INTO holdings (symbol, quantity, price, cost_basis)
            VALUES (?, ?, ?, ?)
            """,
            (symbol.upper(), quantity, price, cost_basis),
        )
        conn.commit()
    finally:
        conn.close()

def update_holding(holding_id: int, quantity: float, price: float, cost_basis: float) -> bool:
    conn = get_connection()
    try:
        cursor=conn.execute(
            """
            UPDATE holdings
            SET quantity = ?, price = ?, cost_basis = ?
            WHERE id = ?
            """,
            (quantity, price, cost_basis, holding_id),
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
            SELECT id,symbol, quantity, price, cost_basis
            FROM holdings
            ORDER BY symbol
            """
        ).fetchall()
        return [
            {
                "id": row["id"],
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