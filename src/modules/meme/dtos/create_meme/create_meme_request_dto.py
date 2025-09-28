from typing import Optional

from fastapi import File, Form, UploadFile
from pydantic import BaseModel


class CreateMemeRequestDto(BaseModel):
    title: str = (Form(min_length=1, max_length=255),)
    description: Optional[str] = (Form(None, max_length=1000),)
    image: UploadFile = File(...)
