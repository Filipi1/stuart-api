from modules.shared.adapters import ApplicationService
from modules.user.dtos.fetch_user_by_token.fetch_user_by_token_request_dto import (
    FetchUserByTokenRequestDto,
)
from modules.user.dtos.fetch_user_by_token.fetch_user_by_token_response_dto import (
    FetchUserByTokenResponseDto,
)
from modules.user.exceptions.user_not_found_exception import UserNotFoundException
from modules.user.services.domain.get_user_by_token_service import (
    GetUserByTokenDomainService,
)


class FetchUserByTokenApplicationService(ApplicationService):
    def __init__(self, get_user_by_token: GetUserByTokenDomainService):
        self.get_user_by_token = get_user_by_token

    async def process(
        self, input: FetchUserByTokenRequestDto
    ) -> FetchUserByTokenResponseDto:
        user = await self.get_user_by_token.process(input.token)
        if not user:
            raise UserNotFoundException("User not found")
        return FetchUserByTokenResponseDto(user=user)
