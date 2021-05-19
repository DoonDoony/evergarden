from fastapi import FastAPI
from mangum import Mangum

from evergarden.api.api import api_router
from evergarden.core.config import settings

app = FastAPI()
app.include_router(api_router, prefix=settings.API_URL_PREFIX)
handler = Mangum(app)
