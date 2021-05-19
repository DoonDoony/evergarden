from fastapi import APIRouter
from fastapi.responses import HTMLResponse
from starlette.requests import Request

from evergarden.services.markdown import markdown_service

router = APIRouter()


@router.post("/html", response_class=HTMLResponse)
async def html(request: Request) -> str:
    content = await request.body()
    markdown_text = content.decode("UTF-8")
    return markdown_service.to_html(markdown_text)
