from fastapi import FastAPI

from backend.app.core.config import settings
from backend.app.api.router import api_router

app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
)

app.include_router(api_router)