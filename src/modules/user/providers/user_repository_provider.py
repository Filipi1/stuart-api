from typing import Annotated

from fastapi import Depends

from modules.shared.providers import SupabaseServiceProvider
from modules.user.repositories.user_repository import UserRepository


def user_repository_provider(supabase_service: SupabaseServiceProvider):
    return UserRepository(supabase_service)


UserRepositoryProvider = Annotated[UserRepository, Depends(user_repository_provider)]
