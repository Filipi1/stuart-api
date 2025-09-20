from typing import Annotated
from fastapi import Depends
from modules.meme.providers.get_earned_memes_by_user_provider import (
    GetEarnedMemesByUserServiceProvider,
)
from modules.meme.services.application import FetchEarnedMemesByUserApplicationService


def fetch_earned_memes_by_user_provider(
    get_earned_memes_by_user: GetEarnedMemesByUserServiceProvider,
):
    return FetchEarnedMemesByUserApplicationService(get_earned_memes_by_user)


FetchEarnedMemesByUserServiceProvider = Annotated[
    FetchEarnedMemesByUserApplicationService,
    Depends(fetch_earned_memes_by_user_provider),
]
