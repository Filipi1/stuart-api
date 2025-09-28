from typing import Annotated

from fastapi import Depends

from modules.meme.repositories.meme_repository import MemeRepository
from modules.shared.providers.supabase_service_provider import SupabaseServiceProvider


def meme_repository_provider(supabase_service: SupabaseServiceProvider):
    return MemeRepository(supabase_service)


MemeRepositoryProvider = Annotated[MemeRepository, Depends(meme_repository_provider)]
