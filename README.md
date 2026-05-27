# ChatBot-Dengue Web App

Aplicação web interativa de conscientização e triagem informativa sobre a dengue para a comunidade universitária e população geral assistida pelo PETSaúde.

## 🚀 Stack Tecnológica
- **Backend:** FastAPI (Python 3.13)
- **Frontend:** HTML5 + Alpine.js + Tailwind CSS (CDN)
- **NLP:** Rapidfuzz (Similaridade local)
- **Deploy:** Railway

## 🛠️ Como Executar Localmente

### Pré-requisitos
- Python 3.13+
- Pip (gerenciador de pacotes)

### Passo a Passo
1. **Clone o repositório:**
   ```bash
   git clone <repo-url>
   cd ChatBot-Dengue-web
   ```

2. **Crie um ambiente virtual:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Prepare os dados:**
   - Certifique-se de que o arquivo `conteudo_petsaude.csv` está na raiz do projeto.
   - Execute o script de importação:
     ```bash
     python scripts/import_csv.py
     ```

5. **Inicie o servidor:**
   ```bash
   uvicorn app.main:app --reload
   ```

## 📂 Estrutura de Pastas
Consulte [docs/architecture.md](docs/architecture.md) para detalhes da estrutura do projeto.

## 🚀 Deploy no Railway

O projeto está configurado para deploy imediato no Railway:

1. **Conecte seu GitHub** ao Railway.
2. **Crie um novo projeto** a partir do repositório.
3. **Configure as Variáveis de Ambiente** no Railway (conforme `.env.example`):
   - `APP_NAME`: Nome da sua aplicação.
   - `CORS_ORIGINS`: `["*"]` ou a URL do seu frontend.
4. **Comando de Start:** O Railway detectará o `requirements.txt` e usará o Procfile (opcional) ou você pode configurar o comando:
   ```bash
   uvicorn app.main:app --host 0.0.0.0 --port $PORT
   ```

## 🛡️ Segurança Clínica e LGPD
Este ChatBot foi desenhado sob princípios de segurança médica:
- **Sem Alucinações:** Respostas baseadas estritamente em dados validados.
- **Detecção de Emergência:** Identificação proativa de sinais de alerta.
- **Privacidade Total:** Nenhum dado do usuário é armazenado no servidor.
