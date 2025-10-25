from typing import Annotated

from fastapi import Depends

from modules.meme.providers.get_memes_count_service_provider import (
    GetMemesCountDomainProvider,
)
from modules.meme.services.application.fetch_current_memes_count import (
    FetchCurrentMemesCountApplicationService,
)


def fetch_current_memes_count_provider(
    get_memes_count: GetMemesCountDomainProvider,
):
    return FetchCurrentMemesCountApplicationService(get_memes_count)


FetchCurrentMemesCountServiceProvider = Annotated[
    FetchCurrentMemesCountApplicationService,
    Depends(fetch_current_memes_count_provider),
]
