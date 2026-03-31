import pytest
import subprocess
import time
import requests
from pathlib import Path

# Fixture to start the FastAPI server
@pytest.fixture(scope="session")
def fastapi_server():
    # Path to the backend
    backend_dir = Path(__file__).parent.parent / "backend"
    # Start uvicorn server
    process = subprocess.Popen(
        [r"c:\Users\vivek\Documents\Github\local-robo-advisor\backend\.venv\Scripts\python.exe", "-m", "uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"],
        cwd=backend_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE
    )
    # Wait for server to start
    time.sleep(2)  # Give it time to start
    # Check if server is running
    try:
        response = requests.get("http://127.0.0.1:8000/api/dashboard", timeout=5)
        assert response.status_code == 200
    except:
        process.terminate()
        process.wait()
        raise RuntimeError("Failed to start FastAPI server")
    
    yield "http://127.0.0.1:8000"
    
    # Cleanup
    process.terminate()
    process.wait()