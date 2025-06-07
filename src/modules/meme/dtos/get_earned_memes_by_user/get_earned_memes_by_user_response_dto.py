from pydantic import BaseModel
from modules.meme.entities.earned_meme import EarnedMemeEntity


class GetEarnedMemesByUserResponseDto(BaseModel):
    memes: list[EarnedMemeEntity]
