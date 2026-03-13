from http import HTTPMethod

from modules.coach.dtos.create_coach.create_coach_request_dto import (
    CreateCoachRequestDto,
)
from modules.coach.dtos.create_coach.create_coach_response_dto import (
    CreateCoachResponseDto,
)
from modules.coach.dtos.fetch_random_coach.fetch_random_coach_response_dto import (
    FetchRandomCoachResponseDto,
)
from modules.coach.providers import CreateCoachProvider, FetchRandomCoachProvider
from modules.shared.adapters import APIController
from modules.shared.decorators import API


@API.controller("coach", tags=["Coach"])
class CoachController(APIController):
    @API.route("/", method=HTTPMethod.GET, response_model=FetchRandomCoachResponseDto)
    async def get_coach(self, fetch_random_coach: FetchRandomCoachProvider):
        return await fetch_random_coach.process()

    @API.route("/", method=HTTPMethod.POST, response_model=CreateCoachResponseDto)
    async def create_coach(
        self, body: CreateCoachRequestDto, create_coach: CreateCoachProvider
    ):
        return await create_coach.process(body.message, body.author)
