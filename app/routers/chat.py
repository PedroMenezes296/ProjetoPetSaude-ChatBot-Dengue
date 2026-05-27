from fastapi import APIRouter, Request, HTTPException
from app.schemas.chat_schema import ChatRequest, ChatResponse
from app.services.nlp_service import NLPService
from app.main import limiter
from app.utils.data_loader import DataLoader

from app.services.emergency_service import EmergencyService

router = APIRouter()
nlp_service = NLPService()
emergency_service = EmergencyService()

FALLBACK_MESSAGE = "Desculpe, não consegui compreender sua dúvida. Você pode tentar reformular a pergunta ou escolher uma das opções abaixo no menu."

@router.post("/chat", response_model=ChatResponse)
@limiter.limit("5/10 seconds")
async def chat_interaction(request: Request, chat_req: ChatRequest):
    """
    Processa a interação do usuário via texto livre ou botão.
    Retorna a resposta homologada ou aciona a regra de fallback.
    Verifica também gatilhos de emergência.
    """
    user_text = chat_req.text.strip()
    
    # Verificação de Emergência (Prioridade de segurança)
    is_emergency = emergency_service.is_emergency(user_text)
    
    # Validação redundante de tamanho
    if len(user_text) > 250:
        raise HTTPException(status_code=400, detail="O texto excede o limite de 250 caracteres.")

    # Se for botão, procuramos o título exato primeiro
    if chat_req.is_button:
        data = DataLoader().get_all()
        for item in data:
            if item['titulo'].lower() == user_text.lower():
                return ChatResponse(
                    text=item['texto'],
                    category=item['titulo'],
                    is_emergency=is_emergency,
                    source=item['fonte'],
                    similarity_score=100.0
                )

    # Processamento NLP
    match, score = nlp_service.find_best_match(user_text)

    if match:
        return ChatResponse(
            text=match['texto'],
            category=match['titulo'],
            is_emergency=is_emergency,
            source=match['fonte'],
            similarity_score=score
        )

    # Regra de Fallback
    return ChatResponse(
        text=FALLBACK_MESSAGE,
        category="fallback",
        is_emergency=is_emergency,
        similarity_score=score
    )
