import base64
import uuid
from datetime import datetime
from typing import Optional

from modules.shared.services.image_builder import ImageBuilderService
from modules.fakenews.services.domain.headline_generator_service import HeadlineGeneratorService
from modules.fakenews.entities.fake_news import FakeNews
from modules.fakenews.dtos.create_fake_news import CreateFakeNewsRequestDto, CreateFakeNewsResponseDto


class CreateFakeNewsService:
    
    def __init__(self, image_builder_service: ImageBuilderService, headline_generator_service: HeadlineGeneratorService):
        self.image_builder_service = image_builder_service
        self.headline_generator_service = headline_generator_service
    
    def execute(self, request: CreateFakeNewsRequestDto) -> CreateFakeNewsResponseDto:
        try:
            headline, subtitle = self.headline_generator_service.generate_headline(request.name)
            
            image_data = base64.b64decode(request.image_base64)
            
            fake_news_image = self.image_builder_service.create_fake_news_image(
                image_data=image_data,
                headline=headline,
                subtitle=subtitle
            )
            
            fake_news = FakeNews(
                id=str(uuid.uuid4()),
                name=request.name,
                headline=headline,
                image_base64=fake_news_image,
                created_at=datetime.now().isoformat()
            )
            
            return CreateFakeNewsResponseDto(
                id=fake_news.id,
                name=fake_news.name,
                headline=fake_news.headline,
                image_base64=fake_news.image_base64,
                created_at=fake_news.created_at
            )
            
        except Exception as e:
            raise ValueError(f"Erro ao criar notícia falsa: {str(e)}")
