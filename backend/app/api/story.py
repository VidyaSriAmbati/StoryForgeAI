from fastapi import APIRouter

from backend.app.schemas.story import (
    StoryRequest,
    StoryResponse,
)

from backend.app.services.story_service import (
    generate_story,
)

router = APIRouter(
    prefix="/story",
    tags=["Story"],
)


@router.post(
    "/generate",
    response_model=StoryResponse,
)
def create_story(request: StoryRequest):
    return generate_story(request.prompt)