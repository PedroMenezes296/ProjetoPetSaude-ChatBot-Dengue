import pytest
from httpx import AsyncClient, ASGITransport
from app.main import app

@pytest.mark.asyncio
async def test_chat_button_exact_match():
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/chat", json={"text": "Sintomas", "is_button": True})
    
    assert response.status_code == 200
    data = response.json()
    assert "febre alta" in data["text"]
    assert data["category"] == "Sintomas"
    assert data["similarity_score"] == 100.0

@pytest.mark.asyncio
async def test_chat_nlp_similarity_match():
    # "Como evitar o mosquito" deve dar match com "Prevenção" via palavras-chave
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/chat", json={"text": "como evitar o mosquito", "is_button": False})
    
    assert response.status_code == 200
    data = response.json()
    assert "eliminar focos de água parada" in data["text"]
    assert data["category"] == "Prevenção"
    assert data["similarity_score"] >= 60.0

@pytest.mark.asyncio
async def test_chat_fallback():
    # Texto sem sentido que não deve atingir 60%
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/chat", json={"text": "receita de bolo de chocolate", "is_button": False})
    
    assert response.status_code == 200
    data = response.json()
    assert "não consegui compreender" in data["text"]
    assert data["category"] == "fallback"
    assert data["similarity_score"] < 60.0

@pytest.mark.asyncio
async def test_chat_input_limit():
    long_text = "a" * 251
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/chat", json={"text": long_text, "is_button": False})
    
    # O Pydantic deve retornar 422 Unprocessable Entity devido ao max_length no schema
    assert response.status_code == 422

@pytest.mark.asyncio
async def test_chat_emergency_trigger():
    # Texto contendo termo crítico "sangue"
    async with AsyncClient(transport=ASGITransport(app=app), base_url="http://test") as ac:
        response = await ac.post("/api/chat", json={"text": "estou com sangue nas fezes", "is_button": False})
    
    assert response.status_code == 200
    data = response.json()
    assert data["is_emergency"] is True
    # Deve dar match com Emergência ou Fallback, mas a flag deve estar ativa
    assert "sangue" in data["text"] or data["category"] == "fallback" or data["category"] == "Emergência"
