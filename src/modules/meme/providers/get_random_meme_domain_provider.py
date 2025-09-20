from typing import Annotated
from fastapi import Depends
from modules.meme.services.domain.get_random_meme_service import (
    GetRandomMemeDomainService,
)
from modules.meme.providers.meme_repository_provider import MemeRepositoryProvider


def get_random_meme_domain_provider(meme_repository: MemeRepositoryProvider):
    return GetRandomMemeDomainService(meme_repository)


GetRandomMemeDomainProvider = Annotated[
    GetRandomMemeDomainService, Depends(get_random_meme_domain_provider)
]
