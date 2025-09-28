from typing import Annotated

from fastapi import Depends

from modules.coach.providers.get_random_coach_domain_provider import (
    GetRandomCoachDomainProvider,
)
from modules.coach.services.application.fetch_random_coach_service import (
    FetchRandomCoachApplicationService,
)


def fetch_random_coach_provider(get_random_coach: GetRandomCoachDomainProvider):
    return FetchRandomCoachApplicationService(get_random_coach)


FetchRandomCoachProvider = Annotated[
    FetchRandomCoachApplicationService, Depends(fetch_random_coach_provider)
]
