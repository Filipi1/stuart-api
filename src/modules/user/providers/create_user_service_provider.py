from typing import Annotated
from fastapi import Depends
from modules.user.services.domain.create_user_service import CreateUserDomainService
from modules.user.providers.user_repository_provider import UserRepositoryProvider


def create_user_service_provider(user_repository: UserRepositoryProvider):
    return CreateUserDomainService(user_repository)


CreateUserDomainServiceProvider = Annotated[
    CreateUserDomainService, Depends(create_user_service_provider)
]
