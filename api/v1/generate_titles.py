from typing import Optional
from fastapi import FastAPI
from transformers import pipeline
import uvicorn 
from langdetect import detect




app = FastAPI()



@app.post("/detect_lang")
def detect_langage(text: str) -> str:
    return { "detected langage :" : detect(text) }

@app.get("/parhrasing/v1")
async def create_item():
    return {"allen": "walker"}





uvicorn.run(app, port=8000, host="127.0.0.1")