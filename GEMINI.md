🧩 Template de Prompt — Planejamento de Projeto de Software
IDENTIFICAÇÃO DO PROJETO
Nome do projeto: ChatBot-Dengue Web App

Descrição resumida: Aplicação web interativa (Web App) de conscientização e triagem informativa sobre a dengue para a comunidade universitária e população geral assistida pelo PETSaúde. Funciona de forma híbrida: oferece botões de navegação rápida e aceita entrada de texto livre processada por um algoritmo de NLP local que entrega respostas seguras e homologadas.

Inspirações visuais/funcionais: Interfaces modernas de chat e assistentes virtuais de saúde (como o sistema de triagem da Secretaria de Saúde de Campinas).

CONTEXTO GERAL
A dengue continua sendo a principal endemia do Brasil, exigindo esforços massivos de conscientização pública. Para democratizar o acesso à informação confiável e sem barreiras tecnológicas (como a necessidade de baixar aplicativos de mensagens), o projeto foi modelado como uma aplicação web acessível diretamente pelo navegador via QR Codes impressos em Unidades Básicas de Saúde (UBS) e cartazes universitários.

O sistema resolve o problema da acessibilidade imediata e opera sob uma arquitetura híbrida de segurança clínica: o usuário pode clicar em opções comuns ou digitar livremente sua dúvida. Um mecanismo de Processamento de Linguagem Natural (NLP) local interpreta o texto e busca a resposta exata validada pela equipe de saúde no banco de dados fixo, eliminando riscos de alucinação de inteligências artificiais tradicionais e protegendo a integridade das orientações médicas.

STACK DEFINIDA
Backend: FastAPI (Python 3.13)

Frontend: HTML5 + Alpine.js (reatividade leve via atributos x-data, x-on, x-show, sem build step)

UI: Tailwind CSS (via CDN)

Banco de dados: Sem banco de dados relacional (Stateless). Fonte da verdade: Arquivo estático dengue.json compilado via script local

Testes backend: Pytest + HTTPX AsyncClient

Infraestrutura: Railway (Plano gratuito com deploy automatizado via GitHub)

Outros: rapidfuzz (biblioteca leve para cálculo de similaridade e NLP de aproximação) e slowapi (para rate limiting no backend)

ESCOPO MÍNIMO DA API
GET /api/menu
- Descrição: Retorna a estrutura principal de botões e os títulos contidos no dengue.json para construir a interface inicial do usuário.
- Campos: (nenhum)

POST /api/chat
- Descrição: Recebe a interação do usuário (clique de botão ou texto livre). Processa a inteligência de similaridade por palavras-chave e retorna a resposta clínica homologada, além de verificar se há gatilhos de emergência ativa.
- Campos: text, is_button

REGRAS DE NEGÓCIO
Base de Dados (dengue.json)
Deve conter estritamente as categorias validadas pela equipe de saúde: sintomas, alerta, prevencao, criadouros, ubs, mitos e suspeita.

Cada registro deve obrigatoriamente possuir os nós de dados: titulo, texto, palavras_chave (lista de sinônimos para o NLP) e fonte.

O tamanho do arquivo compilado dengue.json não deve ultrapassar o teto de 2 MB para evitar carregamento excessivo de memória RAM.

Processamento de Linguagem Natural Local (NLP)
Quando is_button for falso, o backend utilizará a biblioteca rapidfuzz para calcular a similaridade do texto do usuário com os termos em palavras_chave.

Se a pontuação de similaridade obtida for igual ou superior a 60%, o backend retorna com sucesso o texto oficial daquela categoria.

Se nenhuma categoria atingir a pontuação mínima de 60%, o sistema acionará a Regra de Fallback: retorna uma mensagem padrão amigável informando que não compreendeu e instrui o frontend a exibir novamente o menu de botões para o usuário.

Sinais de Alerta (Gatilhos de Emergência)
O backend manterá uma lista estrita de termos de risco médico crítico mapeados pela equipe de saúde (ex: "sangue", "sangramento", "desmaio", "vomito persistente", "dor forte na barriga").

Caso o texto do usuário contenha qualquer uma dessas palavras críticas, o backend forçará o campo flag "is_emergency": true na resposta da API.

O frontend, ao ler a flag de emergência ativa, deve travar as interações comuns e exibir um banner visual vermelho destacado orientando a busca imediata por atendimento de urgência.

Regras de consistência
O backend é a fonte da verdade absoluta; nenhuma resposta ou texto clínico é gerado dinamicamente ou modificado em tempo de execução.

A sincronização e atualização das respostas devem ser feitas localmente na máquina dos desenvolvedores por meio de um script utilitário (import_csv.py), que lê a planilha conteudo_petsaude.csv revisada e gera o arquivo dengue.json limpo para deploy. O script deve barrar a geração caso existam colunas obrigatórias vazias.

REQUISITOS NÃO FUNCIONAIS
A aplicação deve operar estritamente dentro dos limites de consumo do plano gratuito do Railway (limitação de RAM inferior a 100MB através do uso do rapidfuzz em vez de LLMs ou spacy pesado).

O campo de texto para entrada do usuário deve aceitar um limite estrito de no máximo 250 caracteres. Essa regra deve ser travada no frontend (atributo maxlength="250") e validada no backend (retornando erro 400 Bad Request em caso de violação).

Rate limiting obrigatório nos endpoints de comunicação configurado via slowapi: máximo de 5 requisições a cada 10 segundos por endereço IP. Em caso de abuso, retornar mensagem instruindo o usuário a aguardar.

Anonimato Total (Adequação à LGPD): a aplicação não deve coletar, rastrear ou armazenar nomes, CPFs, IPs de forma identificável ou histórico médico do usuário no servidor.

O backend deve ser completamente Stateless. O gerenciamento do histórico do chat na tela deve ser controlado unicamente pelo navegador do cliente através de sessionStorage em JavaScript.

O frontend gerado deve carregar os estilos de UI (Tailwind CSS via CDN) e os scripts Alpine.js de forma otimizada para carregar instantaneamente em redes móveis 3G e 4G na porta de postos de saúde.

CONTEXTO ADICIONAL
O projeto foi migrado de um modelo inicial baseado em bot do Telegram para este modelo Web App focado em acessibilidade rápida. A equipe técnica (programação) fornecerá a estrutura do arquivo CSV para que a equipe de saúde do PETSaúde possa preencher as perguntas, respostas e sinônimos diretamente no Google Sheets. O fluxo de deploy será contínuo via GitHub integrado ao Railway.

⚙️ METODOLOGIA DE TRABALHO (NÃO ALTERAR)
A seção abaixo define como a IA deve conduzir o projeto. Não modifique.

AGENTES DO PROJETO
Trabalhe como se houvesse três agentes colaborando:

1. Agente Senior Backend/Arquitetura
Responsabilidades: definir arquitetura geral, garantir separação clara de responsabilidades (routers, services, schemas, utils), definir modelos Pydantic para validação de entrada e saída, garantir escalabilidade da API FastAPI, preparar estrutura para fácil manutenção, revisar aderência REST.

2. Agente Pleno Full Stack
Responsabilidades: implementar endpoints FastAPI e páginas HTML+Alpine.js, criar componentes reutilizáveis com x-data e diretivas Alpine.js, garantir integração API↔frontend via fetch nativo, criar formulários com validação de atributos HTML5 (maxlength, required) reforçada pelo backend.

3. Agente Security Reviewer
Responsabilidades: revisar vulnerabilidades, validar regras contra duplicidade, verificar validação de entrada via Pydantic, CORS, rate limiting com slowapi, exposição indevida de dados, tratamento de erros. Nenhum dado vindo do frontend deve ser confiado sem validação no backend.

SKILLS OBRIGATÓRIAS
Backend (FastAPI/Python):
- Separação por responsabilidade: routers/, services/, schemas/, utils/
- Modelos Pydantic para todos os request/response bodies
- Routers enxutos — lógica de negócio nos services
- Testes de integração com Pytest + HTTPX AsyncClient
- Validação de entrada (Pydantic + validadores customizados)
- Tratamento de exceções com HTTPException
- Rate limiting via slowapi
- CORS configurado explicitamente

Frontend (HTML5 + Alpine.js):
- Reatividade declarativa via x-data, x-show, x-if, x-for, x-on, x-model
- Sem build step — Alpine.js e Tailwind carregados via CDN
- Comunicação com a API via fetch nativo dentro de métodos Alpine
- Estado do chat gerenciado em sessionStorage
- Componentização via x-data em elementos reutilizáveis
- Layout responsivo com Tailwind CSS
- Feedback de loading, erro e empty state declarados no HTML

DevOps:
- Estrutura de pastas clara e documentada
- Variáveis de ambiente via arquivo .env + python-dotenv
- README completo com instruções de execução local e deploy no Railway
- Scripts utilitários (import_csv.py) documentados

Qualidade:
- Testes por endpoint (mínimo 1 teste de integração por rota)
- Baixa complexidade ciclomática — sem ifs aninhados excessivos
- Arquivos pequenos e focados
- Baixo acoplamento entre camadas
- Alta coesão dentro de cada módulo
- Documentação por feature

MÉTRICAS DE QUALIDADE
CCN — Complexidade Ciclomática
Funções com baixa complexidade. Sem ifs aninhados excessivos. Routers simples. Fluxos complexos isolados em services.

COV — Cobertura de Testes
Mínimo 1 teste de integração por endpoint obrigatório. Regras de negócio críticas (NLP, emergência, fallback) sempre testadas.

SZ — Tamanho de Arquivos
Routers pequenos. HTML com Alpine.js focado por responsabilidade. Separar em funções/módulos quando crescer.

DEP — Dependências Estruturais
Baixo acoplamento entre camadas. Frontend não conhece lógica interna do backend. Routers dependem apenas de schemas e services. Sem dependências circulares.

CICLO OBRIGATÓRIO POR FEATURE
Para cada feature, seguir este ciclo:

Planejar a feature

Identificar arquivos criados ou alterados

Implementar a menor parte possível

Criar ou atualizar testes

Rodar os testes

Corrigir falhas

Revisar segurança

Revisar métricas CCN, COV, SZ e DEP

Documentar a feature

Só então seguir para a próxima feature

Nenhuma feature é concluída sem: teste passando + validação de segurança + documentação mínima + revisão de arquitetura.

FASES DE IMPLEMENTAÇÃO
Fase 0 — Setup
Estrutura de pastas, dependências (requirements.txt), variáveis de ambiente, script import_csv.py esqueleto, documentação inicial.

Fase 1 — Backend base
Schemas Pydantic, estrutura de routers, carregamento do dengue.json, configuração de CORS e rate limiting, testes de sanidade.

Fase 2 — Endpoint GET /api/menu
Implementação + testes + documentação.

Fase 3 — Endpoint POST /api/chat (NLP + fallback)
Lógica rapidfuzz, regra dos 60%, fallback, testes + documentação.

Fase 4 — Endpoint POST /api/chat (gatilhos de emergência)
Detecção de termos críticos, flag is_emergency, testes + documentação + regras de consistência.

Fase 5 — Frontend base
Layout HTML + Alpine.js + Tailwind, componentes de chat, botões de menu, campo de texto com maxlength.

Fase 6 — Frontend integrado
Integração com API via fetch, exibição de respostas, banner de emergência, sessionStorage para histórico, loading/erro/fallback states.

Fase 7 — Segurança e qualidade
Revisão CORS, rate limiting, validações Pydantic, complexidade, tamanho de arquivos, dependências, documentação.

Fase 8 — Finalização
Todos os testes passando, README revisado, Railway configurado, checklist final de entrega.

DOCUMENTAÇÃO OBRIGATÓRIA
Ao longo do projeto, criar e manter:

README.md — descrição, stack, como rodar localmente, como fazer deploy no Railway, endpoints

docs/architecture.md — decisões arquiteturais, organização de pastas, justificativas

docs/business-rules.md — regras de negócio, casos de erro, lógica NLP, gatilhos de emergência

docs/api.md — endpoints, payloads, responses, códigos de erro

docs/security.md — validações Pydantic, proteções, rate limiting, CORS, LGPD, pontos de atenção

docs/testing.md — estratégia, como rodar (pytest), testes existentes, cobertura mínima

docs/quality-metrics.md — como avaliar CCN, COV, SZ, DEP; critérios de aceite por feature

CRITÉRIOS DE ACEITE GERAIS
Backend: todos os endpoints existem, testes passando, regras críticas testadas (NLP, fallback, emergência), schemas Pydantic definidos, validações funcionando, MVC/separação de responsabilidades respeitada.

Frontend: Alpine.js + HTML responsivo + Tailwind + fluxos completos (menu, chat, emergência, fallback, loading, erro).

Deploy: projeto sobe no Railway sem erros, variáveis de ambiente documentadas, instruções no README.

Qualidade: baixa complexidade, arquivos pequenos, baixo acoplamento, sem vulnerabilidades óbvias, código preparado para evolução.

PRIMEIRA RESPOSTA ESPERADA
Antes de qualquer implementação, responda apenas com:

Análise da stack escolhida

Proposta de arquitetura

Divisão dos agentes e responsabilidades

Regras de negócio refinadas

Métricas de qualidade que serão usadas

Estrutura de pastas proposta

Planejamento por fases

Critérios de aceite

Perguntas essenciais, se houver alguma decisão bloqueante

Não escreva código. Não crie arquivos. Aguarde minha aprovação para iniciar a Fase 0.
