from pydantic import BaseModel


class StoryRequest(BaseModel):
    prompt: str


class StoryResponse(BaseModel):
    title: str
    story: str