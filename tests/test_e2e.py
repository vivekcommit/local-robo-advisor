import pytest
import httpx
from playwright.sync_api import Page

def test_dashboard_loads(fastapi_server, page: Page):
    """Test that the dashboard page loads and displays data."""
    page.goto(fastapi_server)
    
    # Wait for the page to load
    page.wait_for_load_state("networkidle")
    
    # Check that the title is present
    assert "Local Robo Advisor" in page.title()
    
    # Check that total value is displayed (might be - initially)
    total_value = page.locator("#total-value")
    assert total_value.is_visible()
    
    # Check that the refresh button is present
    refresh_btn = page.locator("#refresh-btn")
    assert refresh_btn.is_visible()

def test_api_dashboard(fastapi_server):
    """Test the /api/dashboard endpoint directly."""
    with httpx.Client() as client:
        response = client.get(f"{fastapi_server}/api/dashboard")
        assert response.status_code == 200
        data = response.json()
        assert "message" in data
        assert "summary" in data
        assert "total_value" in data["summary"]
        assert "holdings" in data

def test_api_holdings(fastapi_server):
    """Test the /api/holdings endpoint."""
    with httpx.Client() as client:
        response = client.get(f"{fastapi_server}/api/holdings")
        assert response.status_code == 200
        data = response.json()
        assert isinstance(data, list)  # Should be a list of holdings

def test_add_holding_via_api(fastapi_server):
    """Test adding a holding via API."""
    with httpx.Client() as client:
        # Add a holding
        holding_data = {
            "symbol": "TEST",
            "quantity": 10.0,
            "price": 100.0,
            "cost_basis": 90.0,
            "asset_class": "Test_Asset"
        }
        response = client.post(f"{fastapi_server}/api/holdings", json=holding_data)
        assert response.status_code == 200
        
        # Check that it's in holdings
        response = client.get(f"{fastapi_server}/api/holdings")
        holdings = response.json()
        assert any(h["symbol"] == "TEST" for h in holdings)

def test_browser_interaction(fastapi_server, page: Page):
    """Test browser interaction with the app."""
    page.goto(fastapi_server)
    page.wait_for_load_state("networkidle")
    
    # Click refresh button
    page.locator("#refresh-btn").click()
    
    # Wait a bit for JS to load data
    page.wait_for_timeout(1000)
    
    # Check that data is loaded (assuming there might be data)
    # This is basic; in real scenario, check specific elements
    assert page.locator("#total-value").text_content() != "-"