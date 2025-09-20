from modules.coach.services.domain.create_coach_service import (
    CreateCoachDomainService,
)
from modules.coach.dtos.create_coach.create_coach_response_dto import (
    CreateCoachResponseDto,
)

from modules.shared.adapters import ApplicationService


class CreateCoachApplicationService(ApplicationService):
    def __init__(self, create_coach: CreateCoachDomainService):
        self.__create_coach = create_coach

    async def process(self, message: str, author: str) -> CreateCoachResponseDto:
        coach = await self.__create_coach.process(message, author)

        return CreateCoachResponseDto(
            id=coach.id,
            message=coach.message,
            author=coach.author,
            created_at=coach.created_at,
            updated_at=coach.updated_at,
        )
