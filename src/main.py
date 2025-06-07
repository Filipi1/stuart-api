from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from containers import Containers
from modules.shared.decorators import API

containers = Containers()

app = FastAPI()
API.initialize(app)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def health_check():
    return {"message": "OK"}
