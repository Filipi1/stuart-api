from typing import Annotated
from fastapi import Depends

from modules.auth.services.domain.generate_token_service import (
    GenerateTokenDomainService,
)
from modules.user.providers.get_user_by_username_service_provider import (
    GetUserByUsernameDomainServiceProvider,
)
from modules.user.providers.create_user_service_provider import (
    CreateUserDomainServiceProvider,
)


def generate_token_domain_service_provider(
    get_user_by_username: GetUserByUsernameDomainServiceProvider,
    create_user: CreateUserDomainServiceProvider,
):
    return GenerateTokenDomainService(
        get_user_by_username=get_user_by_username,
        create_user=create_user,
    )


GenerateTokenDomainServiceProvider = Annotated[
    GenerateTokenDomainService, Depends(generate_token_domain_service_provider)
]
