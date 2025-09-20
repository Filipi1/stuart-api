from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.meme_repository import MemeRepository
from modules.shared.adapters import DomainService


class GetRandomMemeDomainService(DomainService):
    def __init__(self, meme_repository: MemeRepository):
        self.__meme_repository = meme_repository
        super().__init__(GetRandomMemeDomainService.__name__)

    async def process(self) -> MemeEntity:
        self.logger.info("Getting random meme...")
        meme = await self.__meme_repository.get_random_meme()
        if not meme:
            self.logger.warning("Meme not found, retrying...")
            await self.process()

        self.logger.info(f"Meme '{meme.title}' found, incrementing earned times...")
        memeUpdated = await self.__meme_repository.increase_earned_times(meme)
        memeUpdated.image = self.__meme_repository.get_storage_url(meme.image)
        self.logger.info(
            f"Meme '{memeUpdated.title}' updated successfully with {memeUpdated.earned_times} earned times"
        )
        return memeUpdated
