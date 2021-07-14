from typing import Optional
from fastapi import FastAPI
from transformers import pipeline
import uvicorn 


question_generation_pipe = pipeline('text2text-generation', model ="JDBN/t5-base-fr-qg-fquad",tokenizer="JDBN/t5-base-fr-qg-fquad")



def generate_question(sentence : str) -> str:
    sentence = "generate question: " + sentence + " </s>"
    return question_generation_pipe(sentence)[0]["generated_text"]



app = FastAPI()




@app.post("/generate_questions")
async def create_item(text: str):
    return {"generated question" :  generate_question(text) }


uvicorn.run(app, port=8000, host="127.0.0.1")