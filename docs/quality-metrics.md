# Métricas de Qualidade

## Critérios de Aceite
1. **CCN (Complexidade Ciclomática):** Todas as funções mantidas abaixo de 5.
2. **SZ (Tamanho de Arquivo):** Nenhum arquivo de lógica excede 150 linhas.
3. **DEP (Dependências):** Separação clara entre Routers, Services e Schemas.

## Auditoria de Código
- **Backend:** Uso consistente de Type Hints e Pydantic Models.
- **Frontend:** Uso de Alpine.js para evitar manipulação direta do DOM, mantendo o código declarativo e limpo.
- **Dados:** Validação rigorosa no script `import_csv.py` para garantir integridade do `dengue.json`.
