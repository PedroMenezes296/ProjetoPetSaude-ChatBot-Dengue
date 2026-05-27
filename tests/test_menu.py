import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_get_menu():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.get("/api/menu")
    
    assert response.status_code == 200
    data = response.json()
    assert "items" in data
    assert len(data["items"]) > 0
    # Verifica se os títulos do mock CSV estão presentes
    titles = [item["title"] for item in data["items"]]
    assert "Sintomas" in titles
    assert "Prevenção" in titles
    assert "Emergência" in titles
