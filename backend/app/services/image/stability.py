import os


def generate(prompt: str):
    """
    Placeholder implementation.

    Later this file will call Stability AI's image generation API.
    """

    api_key = os.getenv("STABILITY_API_KEY")

    if not api_key:
        return {
            "success": False,
            "provider": "Stability AI",
            "error": "NOT_CONFIGURED",
            "message": "Stability AI is not configured.",
        }

    return {
        "success": False,
        "provider": "Stability AI",
        "error": "NOT_IMPLEMENTED",
        "message": "Stability AI integration is not implemented yet.",
    }