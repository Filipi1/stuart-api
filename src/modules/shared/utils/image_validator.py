import io
from typing import Tuple
from PIL import Image
from modules.shared.exceptions.invalid_image_exception import InvalidImageException


class ImageValidator:
    """Utilitário para validação e conversão de imagens"""

    # Formatos válidos suportados
    VALID_FORMATS = [".jpg", ".jpeg", ".png", ".gif"]

    # MIME types válidos
    VALID_MIME_TYPES = ["image/jpeg", "image/jpg", "image/png", "image/gif"]

    @classmethod
    def validate_image(cls, file_content: bytes, filename: str) -> Tuple[bool, str]:
        """
        Valida se o arquivo é uma imagem válida

        Args:
            file_content: Conteúdo do arquivo em bytes
            filename: Nome do arquivo

        Returns:
            Tuple[bool, str]: (é_válida, extensão_do_arquivo)

        Raises:
            InvalidImageException: Se o arquivo não for uma imagem válida
        """
        try:
            # Verifica se consegue abrir como imagem
            image = Image.open(io.BytesIO(file_content))

            # Verifica o formato da imagem
            image_format = image.format.lower() if image.format else ""

            # Verifica se o formato é válido
            if image_format not in ["jpeg", "jpg", "png", "gif"]:
                raise InvalidImageException(
                    f"Formato de imagem '{image_format}' não é suportado"
                )

            # Verifica a extensão do arquivo
            file_extension = cls._get_file_extension(filename).lower()
            if file_extension not in cls.VALID_FORMATS:
                raise InvalidImageException(
                    f"Extensão de arquivo '{file_extension}' não é suportada"
                )

            return True, file_extension

        except Exception as e:
            if isinstance(e, InvalidImageException):
                raise
            raise InvalidImageException("Arquivo não é uma imagem válida")

    @classmethod
    def convert_to_jpg(cls, file_content: bytes, filename: str) -> Tuple[bytes, str]:
        """
        Converte uma imagem para formato JPG

        Args:
            file_content: Conteúdo do arquivo em bytes
            filename: Nome do arquivo original

        Returns:
            Tuple[bytes, str]: (conteúdo_convertido, novo_nome_do_arquivo)
        """
        try:
            # Abre a imagem
            image = Image.open(io.BytesIO(file_content))

            # Converte para RGB se necessário (para suportar PNG com transparência)
            if image.mode in ("RGBA", "LA", "P"):
                # Cria um fundo branco para imagens com transparência
                background = Image.new("RGB", image.size, (255, 255, 255))
                if image.mode == "P":
                    image = image.convert("RGBA")
                background.paste(
                    image, mask=image.split()[-1] if image.mode == "RGBA" else None
                )
                image = background
            elif image.mode != "RGB":
                image = image.convert("RGB")

            # Converte para bytes em formato JPG
            output = io.BytesIO()
            image.save(output, format="JPEG", quality=95, optimize=True)
            output.seek(0)

            # Gera novo nome do arquivo com extensão .jpg
            base_name = cls._get_base_filename(filename)
            new_filename = f"{base_name}.jpg"

            return output.getvalue(), new_filename

        except Exception as e:
            raise InvalidImageException(f"Erro ao converter imagem para JPG: {str(e)}")

    @classmethod
    def process_image(cls, file_content: bytes, filename: str) -> Tuple[bytes, str]:
        """
        Processa uma imagem: valida e converte se necessário

        Args:
            file_content: Conteúdo do arquivo em bytes
            filename: Nome do arquivo

        Returns:
            Tuple[bytes, str]: (conteúdo_processado, nome_do_arquivo_final)
        """
        try:
            # Primeiro tenta validar a imagem
            is_valid, extension = cls.validate_image(file_content, filename)

            # Se a extensão não for .jpg, converte para JPG
            if extension.lower() not in [".jpg", ".jpeg"]:
                return cls.convert_to_jpg(file_content, filename)

            return file_content, filename

        except InvalidImageException:
            # Se não conseguir validar, tenta converter para JPG
            try:
                return cls.convert_to_jpg(file_content, filename)
            except Exception:
                raise InvalidImageException("Não foi possível processar a imagem")

    @staticmethod
    def _get_file_extension(filename: str) -> str:
        """Extrai a extensão do arquivo"""
        if "." in filename:
            return "." + filename.split(".")[-1].lower()
        return ""

    @staticmethod
    def _get_base_filename(filename: str) -> str:
        """Extrai o nome base do arquivo sem extensão"""
        if "." in filename:
            return ".".join(filename.split(".")[:-1])
        return filename
