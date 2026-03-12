# Roadmap

This file tracks what we’ve already built and what we plan to build next for the **Local Robo Advisor** backend.[web:153][web:157]

---

## ✅ Done so far

### M1 – Basic backend and data storage

- Create FastAPI app with simple `/api/dashboard` endpoint.
- Add `/api/holdings` endpoint.
- Introduce `user_data/robo_advisor.db` SQLite database.
- Add `db.py` to manage DB path and `init_db()` for schema creation.
- Implement `services/portfolio.py` with:
  - `get_all_holdings`
  - `add_holding`
  - `update_holding`
  - `delete_holding`
  - `get_dashboard_snapshot`
- Wire FastAPI routes to the service layer.
- Full CRUD API for holdings:
  - `GET /api/holdings`
  - `POST /api/holdings`
  - `PUT /api/holdings/{holding_id}`
  - `DELETE /api/holdings/{holding_id}`
- Basic dashboard:
  - `GET /api/dashboard` returns `total_value` + holdings.[web:159]

---

## 🟡 Next milestones

### M2 – Portfolio analytics

- Add per-holding gain/loss fields (unrealized P&L).
- Add portfolio-level total gain/loss.
- Extend dashboard response to include P&L summary.
- Add simple filters (e.g., by symbol) as query parameters.[web:159][web:156]

### M3 – Tax-loss harvesting experiments

- Add `services/tax_loss.py` with:
  - Function to identify loss positions below cost basis.
  - Simple rules for “sell candidate” suggestions.
- Add API endpoint like `GET /api/tax-loss-opportunities`.
- Document assumptions and limitations in `docs/TAX_LOSS_NOTES.md`.[web:142][web:156]

### M4 – Rebalancing

- Add `services/rebalance.py` with:
  - Target allocation representation (e.g., per asset class).
  - Function to compute drift from target.
- Add endpoint like `POST /api/rebalance/suggestions`.
- Return a human-readable list of suggested trades.

---

## 🔵 Later / nice to have

- Authentication (even simple API key) for local use.
- Unit tests for service functions and routes.
- Frontend dashboard (React/Vue or simple HTML/JS) that:
  - Shows holdings and P&L.
  - Lets you add/update/delete holdings.
  - Visualizes allocation and drift.
- CI workflow (GitHub Actions) to run tests on push.

---

## Notes

- This roadmap is intentionally lightweight and will evolve as we learn from experiments.
- When you complete a milestone, move it from “Next milestones” to “Done so far” and commit the change.
