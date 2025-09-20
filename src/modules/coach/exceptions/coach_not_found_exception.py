from modules.shared.exceptions.application_exception import ApplicationException


class CoachNotFoundException(ApplicationException):
    def __init__(self, message: str = "Coach not found"):
        super().__init__(message)
