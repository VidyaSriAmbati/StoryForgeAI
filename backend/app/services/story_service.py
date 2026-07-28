from backend.app.schemas.story import StoryResponse


def generate_story(prompt: str) -> StoryResponse:
    return StoryResponse(
        title="The Brave Explorer",
        story=f"This is a generated story based on: {prompt}"
    )