from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def home():
    return {
        "message": "Welcome to StoryForge AI 🚀",
        "status": "Running"
    }