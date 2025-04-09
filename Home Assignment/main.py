from fastapi import FastAPI, File, UploadFile, HTTPException
from pydantic import BaseModel
import motor.motor_asyncio
from dotenv import load_dotenv
from bson import ObjectId
import os

load_dotenv()

app = FastAPI()

# Connect to Mongo Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.multimedia_db

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.get("/")
async def root():
    return {"message": "Multimedia API running successfully"}

@app.post("/upload_sprite")
async def upload_sprite(file: UploadFile = File(...)):
    content = await file.read()
    sprite_doc = {"filename": file.filename, "content": content}
    result = await db.sprites.insert_one(sprite_doc)
    return {"message": "Sprite uploaded", "id": str(result.inserted_id)}


@app.post("/upload_audio")
async def upload_audio(file: UploadFile = File(...)):
    content = await file.read()
    audio_doc = {"filename": file.filename, "content": content}
    result = await db.audio.insert_one(audio_doc)
    return {"message": "Audio file uploaded", "id": str(result.inserted_id)}

@app.post("/player_score")
async def post_score(score: PlayerScore):
    result = await db.scores.insert_one(score.dict())
    return {"message": "Score recorded", "id": str(result.inserted_id)}

@app.get("/player_scores")
async def get_scores():
    scores = []
    async for doc in db.player_scores.find():
        doc["_id"] = str(doc["_id"])  # Convert ObjectId to string
        scores.append(doc)
    return scores