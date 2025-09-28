from modules.auth.dtos.authenticate import (
    AuthenticateRequestDto,
    AuthenticateResponseDto,
)

from modules.shared.adapters import ApplicationService
from modules.auth.services.domain.generate_token_service import (
    GenerateTokenDomainService,
)


class AuthenticateApplicationService(ApplicationService):
    def __init__(self, generate_token: GenerateTokenDomainService):
        self.__generate_token = generate_token
        super().__init__(AuthenticateApplicationService.__name__)

    async def process(self, input: AuthenticateRequestDto) -> AuthenticateResponseDto:
        token = await self.__generate_token.process(input.identifier)
        return AuthenticateResponseDto(token=token)
