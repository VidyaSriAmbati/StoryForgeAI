from abc import ABC, abstractmethod


class BaseImageService(ABC):

    @abstractmethod
    def generate_image(self, prompt: str):
        pass