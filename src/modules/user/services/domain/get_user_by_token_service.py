from typing import Optional

from modules.shared.adapters import DomainService
from modules.shared.services.cache.cache_service import CacheService
from modules.user.entities.user import User
from modules.user.enums.user_cache_keys_enum import UserCacheKeysEnum
from modules.user.repositories.user_repository import UserRepository


class GetUserByTokenDomainService(DomainService):
    def __init__(self, user_repository: UserRepository, cache: CacheService):
        self.user_repository = user_repository
        self.__cache = cache
        super().__init__(GetUserByTokenDomainService.__name__)

    def __get_cache_key(self, token: str) -> str:
        return UserCacheKeysEnum.USER.value.format(token=token)

    async def process(self, token: str) -> Optional[User]:
        cache_key = self.__get_cache_key(token)

        async def compute_user():
            return await self.user_repository.get_user_by_token(token)

        return await self.__cache.get_or_compute_model(
            key=cache_key,
            compute_func=compute_user,
            model_class=User,
        )
