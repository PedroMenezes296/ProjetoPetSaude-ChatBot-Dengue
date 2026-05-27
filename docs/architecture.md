# Arquitetura do Sistema

## Organização de Pastas
- `app/`: Código fonte do backend FastAPI.
  - `routers/`: Definição de endpoints.
  - `services/`: Lógica de negócio (NLP, triagem).
  - `schemas/`: Modelos Pydantic (validação).
  - `utils/`: Funções utilitárias e carregadores de dados.
  - `data/`: Armazenamento do `dengue.json`.
- `frontend/`: Arquivos estáticos (HTML/JS/CSS).
- `scripts/`: Scripts de automação e utilitários de dados.
- `docs/`: Documentação técnica detalhada.

## Fluxo de Dados
1. O usuário interage via frontend (Alpine.js).
2. O frontend envia requisições para a API FastAPI.
3. A API processa a similaridade via Rapidfuzz usando o `dengue.json`.
4. A API retorna a resposta homologada.
