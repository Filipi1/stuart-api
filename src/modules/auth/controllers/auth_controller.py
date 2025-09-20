from http import HTTPMethod
from modules.auth.dtos.authenticate.authenticate_request_dto import (
    AuthenticateRequestDto,
)
from modules.auth.dtos.authenticate.authenticate_response_dto import (
    AuthenticateResponseDto,
)
from modules.shared.decorators import API
from modules.shared.adapters import APIController
from containers import containers


@API.controller("auth")
class AuthController(APIController):
    def __init__(self):
        self.__authenticate_application_service = (
            containers.authenticate_application_service
        )

    @API.route("/", method=HTTPMethod.GET, response_model=AuthenticateResponseDto)
    async def authenticate(self, body: AuthenticateRequestDto):
        return await self.__authenticate_application_service.process(body)
