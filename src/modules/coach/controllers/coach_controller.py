from http import HTTPMethod
from modules.coach.dtos.fetch_random_coach.fetch_random_coach_response_dto import (
    FetchRandomCoachResponseDto,
)
from modules.coach.providers import FetchRandomCoachProvider
from modules.shared.decorators import API
from modules.shared.adapters import APIController


@API.controller("coach")
class CoachController(APIController):
    @API.route("/", method=HTTPMethod.GET, response_model=FetchRandomCoachResponseDto)
    async def get_coach(
        self, fetch_random_coach: FetchRandomCoachProvider
    ):
        return await fetch_random_coach.process()
