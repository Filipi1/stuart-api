from modules.album.services.application.fetch_album_service import (
    FetchAlbumApplicationService,
)
from modules.album.services.domain.build_album_slots_service import BuildAlbumSlotsDomainService
from modules.meme.repositories.earned_meme_repository import EarnedMemeRepository
from modules.meme.services.application.fetch_earned_memes_by_user_service import (
    FetchEarnedMemesByUserApplicationService,
)
from modules.meme.services.domain.get_earned_memes_by_user_service import (
    GetEarnedMemesByUserDomainService,
)
from modules.shared.services.supabase.supabase_service import SupabaseService
from modules.user.repositories.user_repository import UserRepository
from pydantic_settings import BaseSettings

from modules.user.services.application.fetch_user_by_token_service import (
    FetchUserByTokenApplicationService,
)
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class Settings(BaseSettings):
    supabase_url: str
    supabase_key: str
    supabase_schema: str

    class Config:
        env_file = ".env"


class Containers:
    settings = Settings()

    supabase_service = SupabaseService(
        url=settings.supabase_url,
        key=settings.supabase_key,
        schema=settings.supabase_schema,
    )
    user_repository = UserRepository(supabase_service)
    earned_meme_repository = EarnedMemeRepository(supabase_service)

    get_user_by_token = GetUserByTokenDomainService(user_repository)
    get_earned_memes_by_user = GetEarnedMemesByUserDomainService(earned_meme_repository)

    fetch_earned_memes_by_user = FetchEarnedMemesByUserApplicationService(
        get_earned_memes_by_user
    )
    fetch_user_by_token = FetchUserByTokenApplicationService(get_user_by_token)
    build_album_slots = BuildAlbumSlotsDomainService()

    fetch_album = FetchAlbumApplicationService(
        get_user_by_token, get_earned_memes_by_user, build_album_slots
    )


containers = Containers()
