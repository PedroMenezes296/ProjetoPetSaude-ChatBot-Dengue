from pydantic import BaseModel, Field, validator
from typing import List, Optional

class ChatRequest(BaseModel):
    text: str = Field(..., max_length=250, description="O texto enviado pelo usuário ou o título do botão.")
    is_button: bool = Field(default=False, description="Indica se a entrada veio de um clique em botão.")

class ChatResponse(BaseModel):
    text: str = Field(..., description="A resposta clínica homologada ou mensagem de fallback.")
    category: Optional[str] = Field(None, description="A categoria identificada (ex: sintomas, alerta).")
    is_emergency: bool = Field(default=False, description="Flag que indica se um gatilho de emergência foi detectado.")
    source: Optional[str] = Field(None, description="A fonte da informação retornada.")
    similarity_score: float = Field(default=0.0, description="A pontuação de similaridade calculada.")

class MenuItem(BaseModel):
    title: str = Field(..., description="O título do botão para o menu principal.")

class MenuResponse(BaseModel):
    items: List[MenuItem]
