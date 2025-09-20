from modules.coach.entities.coach_entity import CoachEntity
from modules.coach.repositories.coach_repository import CoachRepository
from modules.shared.adapters import DomainService


class CreateCoachDomainService(DomainService):
    def __init__(self, coach_repository: CoachRepository):
        self.__coach_repository = coach_repository
        super().__init__(CreateCoachDomainService.__name__)

    async def process(self, message: str, author: str) -> CoachEntity:
        self.logger.info(f"Creating new coach message from author: {author}")

        coach_data = {"message": message, "author": author}

        coach = await self.__coach_repository.create_coach(coach_data)

        self.logger.info(
            f"Coach message '{coach.message}' created successfully with ID: {coach.id}"
        )
        return coach
