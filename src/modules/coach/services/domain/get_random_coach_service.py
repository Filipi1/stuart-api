from modules.coach.entities.coach_entity import CoachEntity
from modules.coach.repositories.coach_repository import CoachRepository
from modules.shared.adapters import DomainService


class GetRandomCoachDomainService(DomainService):
    def __init__(self, coach_repository: CoachRepository):
        self.__coach_repository = coach_repository
        super().__init__(GetRandomCoachDomainService.__name__)

    async def process(self) -> CoachEntity:
        self.logger.info("Getting random coach...")
        coach = await self.__coach_repository.get_random_coach()
        if not coach:
            self.logger.warning("Coach not found, retrying...")
            await self.process()

        self.logger.info(f"Coach message '{coach.message}' found successfully")
        return coach
