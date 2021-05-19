from fastapi import APIRouter
from starlette.requests import Request

router = APIRouter()


@router.post("/html")
async def html(request: Request) -> bytes:
    return await request.body()
