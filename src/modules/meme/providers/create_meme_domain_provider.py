from typing import Annotated
from fastapi import Depends
from modules.meme.services.domain.create_meme_service import CreateMemeDomainService
from modules.meme.providers.meme_repository_provider import MemeRepositoryProvider


def create_meme_domain_provider(meme_repository: MemeRepositoryProvider):
    return CreateMemeDomainService(meme_repository)


CreateMemeDomainProvider = Annotated[
    CreateMemeDomainService, Depends(create_meme_domain_provider)
]
