import base64

from google.genai import types

from backend.app.services.story_service import client


def generate(prompt: str):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-image",
            contents=prompt,
            config=types.GenerateContentConfig(
                response_modalities=["TEXT", "IMAGE"]
            ),
        )

        for part in response.candidates[0].content.parts:
            if getattr(part, "inline_data", None):
                image_base64 = base64.b64encode(part.inline_data.data).decode("utf-8")

                return {
                    "success": True,
                    "provider": "Gemini",
                    "image": image_base64,
                }

        return {
            "success": False,
            "provider": "Gemini",
            "error": "NO_IMAGE",
            "message": "Gemini did not return an image.",
        }

    except Exception as e:
        error = str(e)

        if "RESOURCE_EXHAUSTED" in error or "429" in error:
            return {
                "success": False,
                "provider": "Gemini",
                "error": "QUOTA_EXCEEDED",
                "message": "Gemini image quota exceeded. Trying another provider.",
            }

        if "404" in error:
            return {
                "success": False,
                "provider": "Gemini",
                "error": "MODEL_NOT_FOUND",
                "message": "Gemini image model unavailable.",
            }

        return {
            "success": False,
            "provider": "Gemini",
            "error": "UNKNOWN",
            "message": str(e),
        }