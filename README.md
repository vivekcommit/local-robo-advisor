# Local Robo Advisor

A local, file-backed robo-advisor backend built with FastAPI and SQLite.

It tracks investment holdings in a local SQLite database, exposes a simple CRUD API for managing positions, and computes a basic portfolio dashboard. The long-term goal is to experiment with tax-loss harvesting and rebalancing logic similar to robo-advisors, but fully local and transparent.

---

## Features

- FastAPI backend with automatic interactive docs at `/docs` and `/redoc`.
- SQLite database stored locally in `user_data/robo_advisor.db`.
- CRUD API for holdings:
  - `GET /api/holdings`
  - `POST /api/holdings`
  - `PUT /api/holdings/{holding_id}`
  - `DELETE /api/holdings/{holding_id}`
- Portfolio dashboard:
  - `GET /api/dashboard` returns total portfolio value plus holdings detail.

---

## Tech Stack

- Python 3.11
- FastAPI
- Uvicorn
- SQLite (`sqlite3` standard library module)
- VS Code for development

---

## Project Structure

```text
local-robo-advisor/
  backend/
    app/
      main.py          # FastAPI app, routes, lifespan startup
      db.py            # SQLite connection + schema init
      services/
        __init__.py
        portfolio.py   # Holdings + dashboard service functions
    .venv/             # Local virtual environment (ignored by git)
  docs/
    ARCHITECTURE.md
  user_data/
    robo_advisor.db    # Local SQLite database (created at runtime)
  README.md
  .gitignore
