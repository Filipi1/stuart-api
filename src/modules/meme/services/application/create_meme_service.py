from typing import Optional
from fastapi import UploadFile
from modules.meme.dtos.create_meme.create_meme_response_dto import CreateMemeResponseDto
from modules.meme.services.domain.create_meme_service import CreateMemeDomainService
from modules.shared.adapters import ApplicationService


class CreateMemeApplicationService(ApplicationService):
    def __init__(self, create_meme_domain_service: CreateMemeDomainService):
        self.__create_meme_domain_service = create_meme_domain_service
        super().__init__(CreateMemeApplicationService.__name__)

    async def process(
        self, title: str, description: Optional[str], image: UploadFile
    ) -> CreateMemeResponseDto:
        file = await image.read()
        meme = await self.__create_meme_domain_service.process(
            title=title, description=description, filename=image.filename, file=file
        )
        return CreateMemeResponseDto(
            id=meme.id,
            title=meme.title,
            description=meme.description,
            image=meme.image,
            earned_times=meme.earned_times,
            created_at=meme.created_at,
            updated_at=meme.updated_at,
        )
