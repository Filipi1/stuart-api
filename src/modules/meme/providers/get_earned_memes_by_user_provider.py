from typing import Annotated

from fastapi import Depends

from modules.meme.providers.earned_memes_repository_provider import (
    EarnedMemesRepositoryProvider,
)
from modules.meme.services.domain.get_earned_memes_by_user_service import (
    GetEarnedMemesByUserDomainService,
)


def get_earned_memes_by_user_provider(
    earned_meme_repository: EarnedMemesRepositoryProvider,
):
    return GetEarnedMemesByUserDomainService(earned_meme_repository)


GetEarnedMemesByUserServiceProvider = Annotated[
    GetEarnedMemesByUserDomainService, Depends(get_earned_memes_by_user_provider)
]
