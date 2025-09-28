from typing import Annotated

from fastapi import Depends

from modules.coach.providers.create_coach_domain_provider import (
    CreateCoachDomainProvider,
)
from modules.coach.services.application.create_coach_service import (
    CreateCoachApplicationService,
)


def create_coach_provider(create_coach: CreateCoachDomainProvider):
    return CreateCoachApplicationService(create_coach)


CreateCoachProvider = Annotated[
    CreateCoachApplicationService, Depends(create_coach_provider)
]
