from backend.app.services.image.factory import generate_image


def create_image(prompt: str):
    return generate_image(prompt)