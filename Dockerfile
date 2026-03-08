FROM python:3.12-slim AS builder

ENV UV_COMPILE_BYTECODE=1 \
    UV_LINK_MODE=copy \
    UV_NO_SYNC=1

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /usr/local/bin/

WORKDIR /app

COPY pyproject.toml uv.lock ./
RUN uv export --frozen --no-dev --format requirements-txt -o requirements.txt \
    && uv pip install --system --target /app/deps -r requirements.txt

FROM python:3.12-slim AS runtime

RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/* \
    && groupadd --gid 1000 appuser \
    && useradd --uid 1000 --gid appuser --shell /bin/bash --create-home appuser

WORKDIR /app

COPY --from=builder --chown=appuser:appuser /app/deps /app/deps
COPY --chown=appuser:appuser pyproject.toml ./
COPY --chown=appuser:appuser src ./src

ENV PYTHONPATH="/app/src:/app/deps"

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONFAULTHANDLER=1 \
    PYTHONBREAKPOINT=disable \
    PYTHONOPTIMIZE=1

LABEL org.opencontainers.image.title="stuart-api" \
      org.opencontainers.image.description="Stuart Meme Manager API"

USER appuser

CMD ["sh", "-c", "python -m uvicorn main:app --host 0.0.0.0 --port ${PORT:-10300} --access-log --log-level info"]
