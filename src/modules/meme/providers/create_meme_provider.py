from typing import Annotated
from fastapi import Depends
from modules.meme.services.application.create_meme_service import (
    CreateMemeApplicationService,
)
from modules.meme.providers.create_meme_domain_provider import CreateMemeDomainProvider


def create_meme_provider(create_meme_domain: CreateMemeDomainProvider):
    return CreateMemeApplicationService(create_meme_domain)


CreateMemeProvider = Annotated[
    CreateMemeApplicationService, Depends(create_meme_provider)
]
