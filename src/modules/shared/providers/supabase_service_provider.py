from typing import Annotated

from fastapi import Depends

from modules.shared.services.supabase.supabase_service import SupabaseService
from modules.shared.settings.settings import Settings


def settings_provider():
    return Settings()


def supabase_service_provider(settings: Settings = Depends(settings_provider)):
    return SupabaseService(
        url=settings.supabase_url,
        key=settings.supabase_key,
        schema=settings.environment == "development" and "staging" or "public",
    )


SupabaseServiceProvider = Annotated[SupabaseService, Depends(supabase_service_provider)]
