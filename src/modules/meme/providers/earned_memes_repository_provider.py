from typing import Annotated

from fastapi import Depends

from modules.meme.repositories.earned_meme_repository import EarnedMemeRepository
from modules.shared.providers import SupabaseServiceProvider


def earned_memes_repository_provider(supabase_service: SupabaseServiceProvider):
    return EarnedMemeRepository(supabase_service)


EarnedMemesRepositoryProvider = Annotated[
    EarnedMemeRepository, Depends(earned_memes_repository_provider)
]
