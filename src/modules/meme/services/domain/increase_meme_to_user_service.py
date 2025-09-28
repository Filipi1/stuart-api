from modules.meme.entities.earned_meme import EarnedMemeEntity
from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.earned_meme_repository import EarnedMemeRepository
from modules.shared.adapters import DomainService
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class IncreaseMemeToUserDomainService(DomainService):
    def __init__(
        self,
        get_user_by_token: GetUserByTokenDomainService,
        earned_meme_repository: EarnedMemeRepository,
    ):
        self.__get_user_by_token = get_user_by_token
        self.__earned_meme_repository = earned_meme_repository
        super().__init__(IncreaseMemeToUserDomainService.__name__)

    async def process(self, meme: MemeEntity, user_token: str) -> EarnedMemeEntity:
        self.logger.info("Increasing meme to user...")
        user = await self.__get_user_by_token.process(user_token)
        if not user:
            raise ValueError("User not found")
        self.logger.info(f"User found: {user.username}")

        earned_meme = await self.__earned_meme_repository.increase_meme_to_user(
            user.id, meme.id
        )
        return earned_meme
