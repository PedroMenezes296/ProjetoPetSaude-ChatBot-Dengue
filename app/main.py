import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded
from dotenv import load_dotenv

# Carrega variáveis de ambiente
load_dotenv()

# Configuração do Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app = FastAPI(
    title=os.getenv("APP_NAME", "ChatBot Dengue"),
    version="1.0.0"
)

app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

# Configuração de CORS
origins = os.getenv("CORS_ORIGINS", "[\"*\"]")
import json
try:
    origins_list = json.loads(origins)
except:
    origins_list = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins_list,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

from app.routers import menu, chat

# Include routers
app.include_router(menu.router, prefix="/api")
app.include_router(chat.router, prefix="/api")

# Serve static files
# Ensure the directory exists
os.makedirs("frontend/assets", exist_ok=True)
app.mount("/assets", StaticFiles(directory="frontend/assets"), name="assets")

@app.get("/")
async def serve_index():
    return FileResponse("frontend/index.html")

@app.get("/health")
async def health_check():
    return {"status": "healthy", "version": "1.0.0"}
