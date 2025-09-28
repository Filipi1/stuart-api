from modules.shared.adapters import ApplicationService
from modules.user.dtos.fetch_user_by_username import (
    FetchUserByUsernameRequestDto,
    FetchUserByUsernameResponseDto,
)
from modules.user.exceptions.user_not_found_exception import UserNotFoundException
from modules.user.services.domain.get_user_by_username_service import (
    GetUserByUsernameDomainService,
)


class FetchUserByUsernameApplicationService(ApplicationService):
    def __init__(self, get_user_by_username: GetUserByUsernameDomainService):
        self.get_user_by_username = get_user_by_username

    async def process(
        self, input: FetchUserByUsernameRequestDto
    ) -> FetchUserByUsernameResponseDto:
        user = await self.get_user_by_username.process(input.username)
        if not user:
            raise UserNotFoundException("User not found")
        return FetchUserByUsernameResponseDto(user=user)
