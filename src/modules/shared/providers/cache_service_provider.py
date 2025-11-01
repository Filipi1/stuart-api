from typing import Annotated

from fastapi import Depends

from modules.shared.services.cache.cache_service import CacheService
from modules.shared.settings.settings import Settings


def settings_provider():
    return Settings()


def cache_service_provider(settings: Settings = Depends(settings_provider)):
    return CacheService(
        host=settings.redis_host or "localhost",
        port=settings.redis_port or 6379,
        db=settings.redis_db or 0,
        password=settings.redis_password,
    )


CacheServiceProvider = Annotated[CacheService, Depends(cache_service_provider)]

