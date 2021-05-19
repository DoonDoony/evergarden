from fastapi import APIRouter

from evergarden.api.endpoints import markdown

api_router = APIRouter()
api_router.include_router(markdown.router, prefix="/markdown", tags=["markdown"])
