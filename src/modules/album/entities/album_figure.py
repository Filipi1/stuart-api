from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class AlbumFigureEntity(BaseModel):
    name: str
    description: Optional[str]
    image: Optional[str]
    drawed_times: int
    earned_at: Optional[datetime]
