import json
from backend.app.services.story_service import client
from backend.app.core.config import settings


def analyze_story(story: str):
    prompt = f"""
You are an expert screenplay analyst.

Analyze the following story.

Return ONLY valid JSON in this format:

{{
    "summary":"...",
    "characters":["...","..."],
    "scenes":[
        {{
            "scene":1,
            "description":"...",
            "visual_prompt":"..."
        }}
    ]
}}

Story:
{story}
"""

    response = client.responses.create(
        model=settings.OPENAI_MODEL,
        input=prompt,
    )

    text = response.output_text.strip()

    return json.loads(text)
    