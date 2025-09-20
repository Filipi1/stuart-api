from typing import Annotated
from fastapi import Depends
from modules.coach.services.domain.get_random_coach_service import (
    GetRandomCoachDomainService,
)
from modules.coach.providers.coach_repository_provider import CoachRepositoryProvider


def get_random_coach_domain_provider(coach_repository: CoachRepositoryProvider):
    return GetRandomCoachDomainService(coach_repository)


GetRandomCoachDomainProvider = Annotated[
    GetRandomCoachDomainService, Depends(get_random_coach_domain_provider)
]
