# Add this at the bottom of main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from pydantic import BaseModel
import motor.motor_asyncio
from fastapi import File, UploadFile, HTTPException
from dotenv import load_dotenv
import os

load_dotenv()

app = FastAPI()

# Connect to MongoDB Atlas
client = motor.motor_asyncio.AsyncIOMotorClient(os.getenv("MONGO_URI"))
db = client.multimedia_db

class PlayerScore(BaseModel):
    player_name: str
    score: int

@app.get("/")
async def root():
    return {"message": "API is working!"}

@app.post("/player_score")
async def add_score(score: PlayerScore):
    result = await db.scores.insert_one(score.dict())
    return {"message": "Score recorded", "id": str(result.inserted_id)}

@app.get("/player_scores")
async def get_scores():
    scores = await db.scores.find().to_list(100)
    return scores

# Adapter for Vercel
# This makes FastAPI work as a handler Vercel can run
def handler(request, context):
    from mangum import Mangum
    asgi_handler = Mangum(app)
    return asgi_handler(request, context)
