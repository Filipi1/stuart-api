from pydantic import Field


class FetchUserByUsernameRequestDto:
    username: str = Field(min_length=1)
