from src.modules.auth.dtos.authenticate import (
    AuthenticateRequestDto,
    AuthenticateResponseDto,
)

from src.modules.shared.adapters import ApplicationService


class AuthenticateApplicationService(ApplicationService):
    def process(self, input: AuthenticateRequestDto) -> AuthenticateResponseDto:
        pass
