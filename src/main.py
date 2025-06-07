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
    user = await containers.user_repository.get_user_by_token("bb31502mc563zqxcx5pj25")
    earned_memes = await containers.earned_meme_repository.get_earned_memes_by_user_id(
        user.id
    )
    return {"message": "OK", "user": user, "earned_memes": earned_memes}
