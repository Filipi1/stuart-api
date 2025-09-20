from typing import Annotated
from fastapi import Depends
from modules.user.providers.user_repository_provider import UserRepositoryProvider
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


def get_user_by_token_service_provider(user_repository: UserRepositoryProvider):
    return GetUserByTokenDomainService(user_repository)


GetUserByTokenServiceProvider = Annotated[
    GetUserByTokenDomainService, Depends(get_user_by_token_service_provider)
]
