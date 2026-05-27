# Documentação da API

## Base URL
A API é servida no mesmo domínio do frontend. Em desenvolvimento local, geralmente `http://localhost:8000`.

## Endpoints

### 1. GET /api/menu
Retorna a lista de títulos de categorias disponíveis para os botões do menu.

**Response:**
```json
{
  "items": [
    { "title": "Sintomas" },
    { "title": "Prevenção" }
  ]
}
```

### 2. POST /api/chat
Processa a interação do usuário e retorna a orientação clínica.

**Request Body:**
```json
{
  "text": "string (max 250 chars)",
  "is_button": "boolean"
}
```

**Response:**
```json
{
  "text": "Conteúdo da orientação...",
  "category": "Sintomas",
  "is_emergency": false,
  "source": "Ministério da Saúde",
  "similarity_score": 100.0
}
```

## Códigos de Erro
- `400 Bad Request`: Input inválido ou texto muito longo.
- `422 Unprocessable Entity`: Falha na validação Pydantic.
- `429 Too Many Requests`: Limite de requisições excedido (5/10s).
