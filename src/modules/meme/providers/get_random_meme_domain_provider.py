from typing import Annotated
from fastapi import Depends
from modules.meme.services.domain.get_random_meme_service import (
    GetRandomMemeDomainService,
)
from modules.meme.providers.meme_repository_provider import MemeRepositoryProvider
from modules.meme.providers.increase_meme_to_user_domain_provider import IncreaseMemeToUserDomainServiceProvider


def get_random_meme_domain_provider(meme_repository: MemeRepositoryProvider, increase_meme_to_user: IncreaseMemeToUserDomainServiceProvider):
    return GetRandomMemeDomainService(increase_meme_to_user, meme_repository)


GetRandomMemeDomainProvider = Annotated[
    GetRandomMemeDomainService, Depends(get_random_meme_domain_provider)
]
