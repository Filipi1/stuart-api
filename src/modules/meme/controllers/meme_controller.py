from http import HTTPMethod
from typing import Optional

from fastapi import File, Form, Header, UploadFile

from modules.meme.dtos.create_meme.create_meme_response_dto import CreateMemeResponseDto
from modules.meme.dtos.fetch_current_memes_count import (
    FetchCurrentMemesCountResponseDto,
)
from modules.meme.dtos.fetch_random_meme.fetch_random_meme_response_dto import (
    FetchRandomMemeResponseDto,
)
from modules.meme.providers import CreateMemeProvider, FetchRandomMemeProvider
from modules.meme.providers.fetch_current_memes_count_provider import (
    FetchCurrentMemesCountServiceProvider,
)
from modules.shared.adapters import APIController
from modules.shared.decorators import API


@API.controller("meme")
class MemeController(APIController):
    @API.route("/", method=HTTPMethod.GET, response_model=FetchRandomMemeResponseDto)
    async def get_meme(
        self,
        fetch_random_meme: FetchRandomMemeProvider,
        x_request_token: Optional[str] = Header(
            None, description="The token of the user"
        ),
    ):
        return await fetch_random_meme.process(x_request_token)

    @API.route("/", method=HTTPMethod.POST, response_model=CreateMemeResponseDto)
    async def create_meme(
        self,
        title: str = Form(..., min_length=1, max_length=255),
        description: Optional[str] = Form(None, max_length=1000),
        image: UploadFile = File(...),
        create_meme: CreateMemeProvider = None,
    ):
        return await create_meme.process(title, description, image)

    @API.route(
        "/status",
        method=HTTPMethod.GET,
        response_model=FetchCurrentMemesCountResponseDto,
    )
    async def get_status(
        self, fetch_current_memes_count: FetchCurrentMemesCountServiceProvider
    ):
        return await fetch_current_memes_count.process()
