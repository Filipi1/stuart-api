from fastapi import Form, File, UploadFile
from pydantic import BaseModel
from typing import Optional


class CreateMemeRequestDto(BaseModel):
    title: str = (Form(min_length=1, max_length=255),)
    description: Optional[str] = (Form(None, max_length=1000),)
    image: UploadFile = File(...)
