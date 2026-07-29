import json

from backend.app.services.story_service import client


def analyze_story(story: str):
    prompt = f"""
You are an expert screenplay analyst.

Analyze the following story.

Return ONLY valid JSON in this format:

{{
    "summary": "...",
    "characters": ["...", "..."],
    "scenes": [
        {{
            "scene": 1,
            "description": "...",
            "visual_prompt": "..."
        }}
    ]
}}

Story:
{story}
"""

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=prompt
    )

    text = response.text.strip()

    # Remove Markdown code fences if Gemini adds them
    text = text.replace("```json", "").replace("```", "").strip()

    return json.loads(text)