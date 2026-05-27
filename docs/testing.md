# Estratégia de Testes

## Execução
Para rodar todos os testes:
```bash
python -m pytest
```

## Cobertura
- **Integração:** 100% dos endpoints (`/health`, `/api/menu`, `/api/chat`) possuem testes automatizados.
- **NLP:** Testes garantem que similaridade acima de 60% retorna a categoria correta e abaixo de 60% aciona o fallback.
- **Emergência:** Testes validam a detecção de termos críticos e ativação da flag `is_emergency`.
- **Limites:** Testes validam a rejeição de inputs acima de 250 caracteres.
