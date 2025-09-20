from pydantic import BaseModel, Field


class CreateCoachRequestDto(BaseModel):
    message: str = Field(
        ..., min_length=1, max_length=1000, description="Mensagem motivacional do coach"
    )
    author: str = Field(
        ..., min_length=1, max_length=255, description="Autor da mensagem"
    )
