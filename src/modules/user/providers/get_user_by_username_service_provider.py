from typing import Annotated
from fastapi import Depends
from modules.user.services.domain.get_user_by_username_service import (
    GetUserByUsernameDomainService,
)
from modules.user.providers.user_repository_provider import UserRepositoryProvider


def get_user_by_username_service_provider(user_repository: UserRepositoryProvider):
    return GetUserByUsernameDomainService(user_repository)


GetUserByUsernameDomainServiceProvider = Annotated[
    GetUserByUsernameDomainService, Depends(get_user_by_username_service_provider)
]
