from typing import Annotated

from fastapi import Depends
from modules.meme.services.application.fetch_random_meme_service import (
    FetchRandomMemeApplicationService,
)
from modules.meme.providers.get_random_meme_domain_provider import GetRandomMemeDomainProvider


def fetch_random_meme_provider(get_random_meme: GetRandomMemeDomainProvider):
    return FetchRandomMemeApplicationService(get_random_meme)


FetchRandomMemeProvider = Annotated[
    FetchRandomMemeApplicationService, Depends(fetch_random_meme_provider)
]
