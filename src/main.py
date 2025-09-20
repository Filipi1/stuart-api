from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from modules.shared.decorators import API
from modules.shared.middleware.correlation_middleware import CorrelationMiddleware

app = FastAPI()
API.initialize(app)


# Adiciona middleware de correlation ID
app.add_middleware(CorrelationMiddleware)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:60404"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    return {"message": "OK"}
