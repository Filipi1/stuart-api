from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.meme_repository import MemeRepository
from modules.shared.adapters import DomainService


class CreateMemeDomainService(DomainService):
    def __init__(self, meme_repository: MemeRepository):
        self.__meme_repository = meme_repository

    async def process(self, title: str, description: str, image: str) -> MemeEntity:
        return await self.__meme_repository.create_meme(title, description, image)
