import sqlite3
from pathlib import Path

# Path to DB file: project_root/user_data/robo_advisor.db
BASE_DIR = Path(__file__).resolve().parents[2]
DB_PATH = BASE_DIR / "user_data" / "robo_advisor.db"

print("DB_PATH is:", DB_PATH)


def get_connection():
    try:
        conn = sqlite3.connect(DB_PATH)
        conn.row_factory = sqlite3.Row
        print("Successfully connected to database at:", DB_PATH)
        return conn
    except Exception as e:
        print("Error connecting to database:", e)
    raise


def init_db():
    try:
        conn = get_connection()
        conn.execute(
            """
            CREATE TABLE IF NOT EXISTS holdings (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                quantity REAL NOT NULL,
                price REAL NOT NULL,
                cost_basis REAL NOT NULL
            )
            """
        )
        conn.commit()
        print("Database initialized successfully.")
    except Exception as e:
            print("Error initializing database:", e)
            raise
    finally:
        try:
            conn.close()
        except Exception:
            print("Error closing database connection.")
            pass

# Temporary function to seed an example holding for testing/demo purposes
def seed_example_holding():
    conn = get_connection()
    try:
        conn.execute(
            """
            INSERT INTO holdings (symbol, quantity, price, cost_basis)
            VALUES (?, ?, ?, ?)
            """,
            ("VTI", 10.0, 250.0, 220.0),
        )
        conn.commit()
        print("Example holding seeded successfully.")
    except Exception as e:
        print("Error seeding example holding:", e)
        raise
    finally:
        try:
            conn.close()
        except Exception:
            print("Error closing database connection.")
            pass
