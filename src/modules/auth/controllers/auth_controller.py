from http import HTTPMethod
from modules.auth.dtos.authenticate.authenticate_request_dto import (
    AuthenticateRequestDto,
)
from modules.auth.dtos.authenticate.authenticate_response_dto import (
    AuthenticateResponseDto,
)
from modules.auth.providers import AuthenticateProvider
from modules.shared.decorators import API
from modules.shared.adapters import APIController


@API.controller("auth")
class AuthController(APIController):
    @API.route("/", method=HTTPMethod.POST, response_model=AuthenticateResponseDto)
    async def authenticate(
        self, body: AuthenticateRequestDto, authenticate_service: AuthenticateProvider
    ):
        return await authenticate_service.process(body)
