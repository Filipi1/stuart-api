from typing import Annotated
from fastapi import Depends
from modules.meme.providers.meme_repository_provider import MemeRepositoryProvider
from modules.meme.services.domain.get_memes_paginated_service import GetMemesPaginatedDomainService

def get_memes_paginated_service_provider(meme_repository: MemeRepositoryProvider):
    return GetMemesPaginatedDomainService(meme_repository)


GetMemesPaginatedServiceProvider = Annotated[
    GetMemesPaginatedDomainService, Depends(get_memes_paginated_service_provider)
]
