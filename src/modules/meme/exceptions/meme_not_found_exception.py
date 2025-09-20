from modules.shared.exceptions.application_exception import ApplicationException


class MemeNotFoundException(ApplicationException):
    def __init__(self, message: str = "Meme not found"):
        super().__init__(message)
