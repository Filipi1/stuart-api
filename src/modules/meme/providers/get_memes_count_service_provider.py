from typing import Annotated

from fastapi import Depends

from modules.meme.providers.meme_repository_provider import MemeRepositoryProvider
from modules.meme.services.domain.get_memes_count_service import (
    GetMemesCountDomainService,
)


def get_memes_count_domain_provider(meme_repository: MemeRepositoryProvider):
    return GetMemesCountDomainService(meme_repository)


GetMemesCountDomainProvider = Annotated[
    GetMemesCountDomainService, Depends(get_memes_count_domain_provider)
]
