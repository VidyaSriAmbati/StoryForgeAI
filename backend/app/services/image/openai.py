import os


def generate(prompt: str):
    """
    Placeholder implementation.

    Later this file will use OpenAI's image generation API.
    """

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        return {
            "success": False,
            "provider": "OpenAI",
            "error": "NOT_CONFIGURED",
            "message": "OpenAI image provider is not configured.",
        }

    return {
        "success": False,
        "provider": "OpenAI",
        "error": "NOT_IMPLEMENTED",
        "message": "OpenAI image generation has not been implemented yet.",
    }