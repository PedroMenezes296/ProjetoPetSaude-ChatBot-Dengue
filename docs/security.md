# Segurança e Privacidade

## LGPD e Privacidade
- **Anonimato:** O sistema não solicita nem armazena nomes, CPFs ou qualquer dado pessoal identificável (PII).
- **Logs:** O backend foi configurado para não logar o corpo das requisições (textos dos usuários).
- **Stateless:** Não há armazenamento de histórico no servidor. O histórico reside apenas no `sessionStorage` do navegador do usuário.

## Proteções de Backend
- **Rate Limiting:** Implementado via `slowapi` (5 requisições a cada 10 segundos por IP).
- **Validação de Input:** Todos os campos são validados via Pydantic. O campo `text` é limitado a 250 caracteres no backend, prevenindo ataques de negação de serviço (DoS) via payloads gigantes.
- **CORS:** Configurado explicitamente via variável de ambiente `CORS_ORIGINS`.

## Segurança Clínica
- **Gatilhos de Emergência:** Uso de expressões regulares estritas para detectar sinais de alerta médico, sobrepondo qualquer lógica de NLP para garantir a segurança do usuário.
- **Fonte da Verdade:** Dados estáticos e validados (`dengue.json`), eliminando riscos de alucinação de IA generativa.
