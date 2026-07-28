from fastapi import APIRouter

from backend.app.api.health import router as health_router
from backend.app.api.story import router as story_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(story_router)