from modules.coach.exceptions.coach_not_found_exception import CoachNotFoundException
from modules.coach.services.domain.get_random_coach_service import (
    GetRandomCoachDomainService,
)
from modules.coach.dtos.fetch_random_coach.fetch_random_coach_response_dto import (
    FetchRandomCoachResponseDto,
)

from modules.shared.adapters import ApplicationService


class FetchRandomCoachApplicationService(ApplicationService):
    def __init__(self, get_random_coach: GetRandomCoachDomainService):
        self.__get_random_coach = get_random_coach

    async def process(self) -> FetchRandomCoachResponseDto:
        coach = await self.__get_random_coach.process()
        if not coach:
            raise CoachNotFoundException("Coach not found")

        return FetchRandomCoachResponseDto(
            id=coach.id,
            message=coach.message,
            author=coach.author,
            created_at=coach.created_at,
            updated_at=coach.updated_at,
        )
