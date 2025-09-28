from .controllers import FakeNewsController
from .dtos.create_fake_news import CreateFakeNewsRequestDto, CreateFakeNewsResponseDto
from .entities import FakeNews

__all__ = [
    "FakeNewsController",
    "FakeNews",
    "CreateFakeNewsRequestDto",
    "CreateFakeNewsResponseDto",
]
