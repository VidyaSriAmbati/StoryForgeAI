from . import gemini
from . import openai
from . import stability

providers = [
    gemini,
    openai,
    stability,
]


def generate_image(prompt: str):
    last_error = None

    for provider in providers:
        print(f"Trying {provider.__name__}...")
        result = provider.generate(prompt)

        if result["success"]:
            print(f"Success from {result['provider']}")
            return result
        print(f"Failed: {result['provider']} - {result['message']}")
        last_error = result

    return last_error