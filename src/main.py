import os

import pytomlpp
from fastapi import FastAPI

from fastapi.middleware.cors import CORSMiddleware

from modules.shared.decorators import API
from modules.shared.settings.settings import Settings
from modules.shared.exceptions.application_exception import ApplicationException
from modules.shared.exceptions.handlers import application_exception_handler
from modules.shared.middleware.correlation_middleware import CorrelationMiddleware

project_info = pytomlpp.load(
    os.path.join(os.path.dirname(os.path.dirname(__file__)), "pyproject.toml")
)
settings = Settings()
app = FastAPI(
    redirect_slashes=False,
    title="Stuart Meme Manager API",
    description="API for the Stuart Meme Manager",
    version=project_info["project"]["version"],
)
API.initialize(app)


app.add_exception_handler(ApplicationException, application_exception_handler)
app.add_middleware(CorrelationMiddleware)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health-check")
async def health_check():
    return {
        "message": f"{app.title} is running",
        "version": app.version,
        "environment": settings.environment or "unknown",
    }

