# Local Robo Advisor

A local, file-backed robo-advisor simulator that automates:
- Tax-loss harvesting
- Portfolio rebalancing
- Dividend reinvestment
- (Planned) Tax-efficient withdrawals
- (Planned) Direct indexing [page:1]

> Educational project. Not investment, tax, or legal advice.

## Current Status

- FastAPI backend skeleton running at `/api/dashboard`
- Fake in-memory holdings and total value
- Next: local database + CSV import
- Later: tax-loss harvesting, rebalancing, dividends, withdrawals [page:1]

## Project Structure

- `backend/` – FastAPI app and business logic.
- `frontend/` – Web UI (to be added).
- `user_data/` – Your local DB and CSVs (gitignored).
- `docs/` – Architecture and roadmap docs.

## Quickstart (Backend)

```bash
cd backend
python -m venv .venv
.venv\Scripts\activate  # Windows
pip install fastapi uvicorn[standard]
uvicorn app.main:app --reload
```

Then visit `http://localhost:8000/api/dashboard` to see the fake data.