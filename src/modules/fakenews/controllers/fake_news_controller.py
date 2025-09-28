import base64
from http import HTTPMethod
from fastapi import HTTPException, status, Form, File, UploadFile
from fastapi.responses import JSONResponse

from modules.shared.adapters.api_controller import APIController
from modules.shared.decorators import API
from modules.fakenews.dtos.create_fake_news import (
    CreateFakeNewsRequestDto,
    CreateFakeNewsResponseDto,
)
from modules.fakenews.services.application.create_fake_news_service import (
    CreateFakeNewsService,
)
from modules.shared.services.image_builder import ImageBuilderService
from modules.fakenews.services.domain.headline_generator_service import (
    HeadlineGeneratorService,
)


@API.controller("fakenews")
class FakeNewsController(APIController):
    def __init__(self):
        self.image_builder_service = ImageBuilderService()
        self.headline_generator_service = HeadlineGeneratorService()
        self.create_fake_news_service = CreateFakeNewsService(
            self.image_builder_service, self.headline_generator_service
        )

    @API.route("/", method=HTTPMethod.POST, response_model=CreateFakeNewsResponseDto)
    async def create_fake_news(
        self,
        name: str = Form(
            ...,
            min_length=1,
            max_length=255,
            description="Nome da pessoa para a notícia falsa",
        ),
        image: UploadFile = File(
            ..., description="Imagem para incluir na notícia falsa"
        ),
    ) -> JSONResponse:
        try:
            if not name or not name.strip():
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST, detail="Nome é obrigatório"
                )

            if not image or not image.filename:
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Imagem é obrigatória",
                )

            if not image.content_type or not image.content_type.startswith("image/"):
                raise HTTPException(
                    status_code=status.HTTP_400_BAD_REQUEST,
                    detail="Arquivo deve ser uma imagem válida",
                )

            image_content = await image.read()

            image_base64 = base64.b64encode(image_content).decode("utf-8")

            request = CreateFakeNewsRequestDto(
                name=name.strip(), image_base64=image_base64
            )

            response = self.create_fake_news_service.execute(request)

            return JSONResponse(
                status_code=status.HTTP_201_CREATED, content=response.__dict__
            )

        except ValueError as e:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail=f"Erro interno do servidor: {str(e)}",
            )
