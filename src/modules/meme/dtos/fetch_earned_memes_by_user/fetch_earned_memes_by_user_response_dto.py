from pydantic import BaseModel

from modules.meme.entities.earned_meme import EarnedMemeEntity


class FetchEarnedMemesByUserResponseDto(BaseModel):
    earned_memes: list[EarnedMemeEntity]
