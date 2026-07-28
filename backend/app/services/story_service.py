import os

from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


def generate_story(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-3.6-flash",
            contents=f"""
Write a creative short story based on this prompt.

Prompt:
{prompt}

Return only the story.
"""
        )

        print(response)

        return {
            "title": "AI Generated Story",
            "story": response.text
        }

    except Exception as e:
        print("ERROR:", repr(e))
        raise