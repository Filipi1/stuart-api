from typing import Optional

from modules.shared.adapters import DomainService
from modules.user.entities.user import User
from modules.user.repositories.user_repository import UserRepository


class GetUserByTokenDomainService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def process(self, token: str) -> Optional[User]:
        user = await self.user_repository.get_user_by_token(token)
        return user
