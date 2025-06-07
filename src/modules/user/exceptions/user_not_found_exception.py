from modules.shared.exceptions.application_exception import ApplicationException


class UserNotFoundException(ApplicationException):
    def __init__(self, message: str = "User not found"):
        super().__init__(message)
