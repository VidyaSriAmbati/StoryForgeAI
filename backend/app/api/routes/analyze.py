from fastapi import APIRouter
from pydantic import BaseModel

from backend.app.services.analysis_service import analyze_story

router = APIRouter(prefix="/analyze", tags=["Analyze"])


class AnalyzeRequest(BaseModel):
    story: str


@router.post("/")
def analyze(request: AnalyzeRequest):
    return analyze_story(request.story)
    