from typing import Annotated

from fastapi import Depends

from modules.meme.providers.meme_repository_provider import MemeRepositoryProvider
from modules.meme.services.domain.create_meme_service import CreateMemeDomainService
from modules.shared.providers.supabase_service_provider import SupabaseServiceProvider


def create_meme_domain_provider(
    meme_repository: MemeRepositoryProvider, supabase_service: SupabaseServiceProvider
):
    return CreateMemeDomainService(meme_repository, supabase_service)


CreateMemeDomainProvider = Annotated[
    CreateMemeDomainService, Depends(create_meme_domain_provider)
]
