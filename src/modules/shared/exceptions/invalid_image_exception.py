from modules.shared.exceptions.application_exception import ApplicationException


class InvalidImageException(ApplicationException):
    def __init__(
        self,
        message: str = "Formato de imagem inválido. Formatos aceitos: PNG, JPG, GIF",
    ):
        super().__init__(message)
