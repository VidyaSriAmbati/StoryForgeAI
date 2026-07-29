from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.image_service import generate_image

router = APIRouter(prefix="/image", tags=["Image"])


class ImageRequest(BaseModel):
    prompt: str


@router.post("/generate")
def generate(req: ImageRequest):
    return generate_image(req.prompt)