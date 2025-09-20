from typing import Annotated
from fastapi import Depends
from modules.auth.services.application.authenticate_service import (
    AuthenticateApplicationService,
)


def authenticate_provider():
    return AuthenticateApplicationService()


AuthenticateProvider = Annotated[
    AuthenticateApplicationService, Depends(authenticate_provider)
]
