from fastapi import APIRouter, Request
from app.schemas.chat_schema import MenuResponse, MenuItem
from app.utils.data_loader import DataLoader
from app.main import limiter

router = APIRouter()

@router.get("/menu", response_model=MenuResponse)
@limiter.limit("5/10 seconds")
async def get_menu(request: Request):
    """
    Retorna a lista de títulos de todas as categorias disponíveis para construir o menu de botões.
    """
    data = DataLoader().get_all()
    items = [MenuItem(title=item['titulo']) for item in data]
    return MenuResponse(items=items)
