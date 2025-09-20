from typing import Optional
import uuid
from modules.meme.entities.meme import MemeEntity
from modules.meme.repositories.meme_repository import MemeRepository
from modules.shared.adapters import DomainService
from modules.shared.services.supabase.supabase_service import SupabaseService
from modules.shared.utils.image_validator import ImageValidator


class CreateMemeDomainService(DomainService):
    def __init__(
        self, meme_repository: MemeRepository, supabase_service: SupabaseService
    ):
        self.__meme_repository = meme_repository
        self.__supabase_service = supabase_service
        super().__init__(CreateMemeDomainService.__name__)

    async def process(
        self, title: str, description: Optional[str], filename: str, file: bytes
    ) -> MemeEntity:
        self.logger.info(f"Creating meme: {title}...")
        processed_image_content, processed_filename = ImageValidator.process_image(
            file, filename
        )
        file_extension = ImageValidator._get_file_extension(processed_filename)
        unique_filename = f"{uuid.uuid4()}{file_extension}"
        await self.__supabase_service.upload_file(
            unique_filename, processed_image_content
        )
        image_url = self.__supabase_service.get_storage_url(unique_filename)
        meme = await self.__meme_repository.create_meme(
            title=title, description=description, image=unique_filename
        )
        self.logger.info(f"Meme created: {meme.title}...")
        meme.image = image_url
        return meme
