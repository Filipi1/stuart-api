from typing import Annotated
from fastapi import Depends
from modules.coach.repositories.coach_repository import CoachRepository
from modules.shared.providers.supabase_service_provider import SupabaseServiceProvider


def coach_repository_provider(supabase_service: SupabaseServiceProvider):
    return CoachRepository(supabase_service)


CoachRepositoryProvider = Annotated[CoachRepository, Depends(coach_repository_provider)]
