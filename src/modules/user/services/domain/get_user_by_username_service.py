from typing import Optional
from modules.user.entities.user import User
from modules.user.repositories.user_repository import UserRepository

from modules.shared.adapters import DomainService


class GetUserByUsernameDomainService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def process(self, username: str) -> Optional[User]:
        user = await self.user_repository.get_user_by_username(username)
        return user
