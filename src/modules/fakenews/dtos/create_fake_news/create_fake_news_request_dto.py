from dataclasses import dataclass


@dataclass
class CreateFakeNewsRequestDto:
    """DTO para requisição de criação de notícia falsa"""

    name: str
    image_base64: str

    def __init__(self, name: str, image_base64: str):
        self.name = name
        self.image_base64 = image_base64
