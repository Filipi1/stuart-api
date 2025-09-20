from modules.meme.dtos.create_meme.create_meme_request_dto import CreateMemeRequestDto
from modules.meme.dtos.create_meme.create_meme_response_dto import CreateMemeResponseDto
from modules.meme.services.domain.create_meme_service import CreateMemeDomainService
from modules.shared.adapters import ApplicationService


class CreateMemeApplicationService(ApplicationService):
    def __init__(self, create_meme_domain_service: CreateMemeDomainService):
        self.__create_meme_domain_service = create_meme_domain_service
        super().__init__(CreateMemeApplicationService.__name__)

    async def process(self, request: CreateMemeRequestDto) -> CreateMemeResponseDto:
        self.logger.info(f"Creating meme: {request.title}...")
        meme = await self.__create_meme_domain_service.process(
            title=request.title, description=request.description, image=request.image
        )
        self.logger.info(f"Meme created: {meme.title}...")

        return CreateMemeResponseDto(
            id=meme.id,
            title=meme.title,
            description=meme.description,
            image=meme.image,
            earned_times=meme.earned_times,
            created_at=meme.created_at,
            updated_at=meme.updated_at,
        )
