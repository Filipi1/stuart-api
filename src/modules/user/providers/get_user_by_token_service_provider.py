from typing import Annotated

from fastapi import Depends

from modules.shared.providers import CacheServiceProvider
from modules.user.providers.user_repository_provider import UserRepositoryProvider
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


def get_user_by_token_service_provider(
    user_repository: UserRepositoryProvider,
    cache: CacheServiceProvider,
):
    return GetUserByTokenDomainService(user_repository, cache)


GetUserByTokenServiceProvider = Annotated[
    GetUserByTokenDomainService, Depends(get_user_by_token_service_provider)
]
