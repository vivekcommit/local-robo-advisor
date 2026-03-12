# Architecture (Simple Overview)

This file explains **how the backend is wired** in plain language.

The goal:  
- A small FastAPI app that talks to a **local SQLite file**.  
- A **service layer** that hides SQL from the API routes.  
- Clean structure so we can add tax-loss and rebalancing later.

---

## 1. Big picture

Data flow for a request:

1. A client calls an API endpoint like `GET /api/holdings`.
2. FastAPI route in `app/main.py` receives the request.
3. That route calls a function in `app/services/portfolio.py`.
4. The service function calls `app/db.py` to read/write SQLite.
5. The result is returned as JSON to the client.

So you can think of it as:

```text
Client → FastAPI route → Service function → SQLite → Service → Route → Client
