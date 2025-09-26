from typing import Annotated
from fastapi import Depends
from modules.auth.services.application.authenticate_service import (
    AuthenticateApplicationService,
)
from modules.auth.providers.generate_token_domain_service_provider import GenerateTokenDomainServiceProvider


def authenticate_provider(generate_token: GenerateTokenDomainServiceProvider):
    return AuthenticateApplicationService(generate_token)


AuthenticateProvider = Annotated[
    AuthenticateApplicationService, Depends(authenticate_provider)
]
