from typing import Optional

from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.meme_repository import MemeRepository
from modules.meme.services.domain.increase_meme_to_user_service import (
    IncreaseMemeToUserDomainService,
)
from modules.shared.adapters import DomainService


class GetRandomMemeDomainService(DomainService):
    def __init__(
        self,
        increase_meme_to_user: IncreaseMemeToUserDomainService,
        meme_repository: MemeRepository,
    ):
        self.__increase_meme_to_user = increase_meme_to_user
        self.__meme_repository = meme_repository
        super().__init__(GetRandomMemeDomainService.__name__)

    async def process(self, user_token: Optional[str] = None) -> MemeEntity:
        self.logger.info("Getting random meme...")
        meme = await self.__meme_repository.get_random_meme()
        if not meme:
            self.logger.warning("Meme not found, retrying...")
            await self.process(user_token)

        if user_token:
            await self.__increase_meme_to_user.process(meme, user_token)

        self.logger.info(f"Meme '{meme.title}' found, incrementing earned times...")
        meme_updated = await self.__meme_repository.increase_earned_times(meme)
        meme_updated.image = self.__meme_repository.get_storage_url(meme.image)
        self.logger.info(
            f"Meme '{meme_updated.title}' updated successfully with {meme_updated.earned_times} earned times"
        )
        return meme_updated
