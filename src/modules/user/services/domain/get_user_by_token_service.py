from typing import Optional
from modules.user.entities.user import User
from modules.user.repositories.user_repository import UserRepository
from modules.user.dtos.get_user_by_token.get_user_by_token_request_dto import (
    GetUserByTokenRequestDto,
)

from modules.shared.adapters import DomainService


class GetUserByTokenDomainService(DomainService):
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def process(self, input: GetUserByTokenRequestDto) -> Optional[User]:
        user = await self.user_repository.get_user_by_token(input.token)
        return user
