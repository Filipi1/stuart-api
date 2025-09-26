from dataclasses import dataclass
from typing import Optional


@dataclass
class FakeNews:
    """Entidade que representa uma notícia falsa gerada"""
    id: str
    name: str
    headline: str
    image_base64: str
    created_at: str
    
    def __init__(self, id: str, name: str, headline: str, image_base64: str, created_at: str):
        self.id = id
        self.name = name
        self.headline = headline
        self.image_base64 = image_base64
        self.created_at = created_at
