# Regras de Negócio

## NLP (Processamento de Linguagem Natural)
- **Threshold:** A similaridade mínima para aceitar uma pergunta é de 60%.
- **Fallback:** Se a similaridade for < 60%, uma mensagem padrão é retornada.

## Emergência (Gatilhos)
- **Palavras Críticas:** O sistema monitora termos como "sangue", "dor forte", "vômito persistente".
- **Ação:** Ativa a flag `is_emergency: true` na resposta.

## Limites
- **Input:** Máximo de 250 caracteres por mensagem.
- **Rate Limit:** Máximo de 5 requisições a cada 10 segundos por IP.
