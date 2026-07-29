from fastapi import APIRouter

from backend.app.api.health import router as health_router
from backend.app.api.story import router as story_router
from backend.app.api.routes.analyze import router as analyze_router
from backend.app.api.image import router as image_router

api_router = APIRouter()

api_router.include_router(health_router)
api_router.include_router(story_router)
api_router.include_router(analyze_router)
api_router.include_router(image_router)