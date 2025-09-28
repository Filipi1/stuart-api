import uuid
from contextvars import ContextVar

from fastapi import Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

# Context variable para armazenar o correlation ID
correlation_id_var: ContextVar[str] = ContextVar("correlation_id", default="")


class CorrelationMiddleware(BaseHTTPMiddleware):
    """Middleware para gerenciar correlation ID em requests"""

    async def dispatch(self, request: Request, call_next):
        # Gera um correlation ID único para cada request
        correlation_id = str(uuid.uuid4())[:8]  # Usa apenas os primeiros 8 caracteres

        # Define o correlation ID no contexto
        correlation_id_var.set(correlation_id)

        # Adiciona o correlation ID no header da response
        response: Response = await call_next(request)
        response.headers["X-Correlation-ID"] = correlation_id

        return response


def get_correlation_id() -> str:
    """Retorna o correlation ID atual do contexto"""
    return correlation_id_var.get()
