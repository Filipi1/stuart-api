from typing import Annotated
from fastapi import Depends
from modules.coach.services.domain.create_coach_service import (
    CreateCoachDomainService,
)
from modules.coach.providers.coach_repository_provider import CoachRepositoryProvider


def create_coach_domain_provider(coach_repository: CoachRepositoryProvider):
    return CreateCoachDomainService(coach_repository)


CreateCoachDomainProvider = Annotated[
    CreateCoachDomainService, Depends(create_coach_domain_provider)
]
