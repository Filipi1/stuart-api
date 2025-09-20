from typing import Annotated

from fastapi import Depends
from modules.user.providers.get_user_by_token_service_provider import (
    GetUserByTokenServiceProvider,
)
from modules.user.services.application.fetch_user_by_token_service import (
    FetchUserByTokenApplicationService,
)


def fetch_user_by_token_service_provider(
    get_user_by_token: GetUserByTokenServiceProvider,
):
    return FetchUserByTokenApplicationService(get_user_by_token)


FetchUserByTokenServiceProvider = Annotated[
    FetchUserByTokenApplicationService, Depends(fetch_user_by_token_service_provider)
]
