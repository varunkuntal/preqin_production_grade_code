from fastapi import FastAPI
from pydantic import BaseModel, validator
from typing import List
import numpy as np

app = FastAPI()

class Sentence(BaseModel):
    text: str

@app.post("/generate_random_vector/", response_model=List[float])
async def generate_random_vector(sentence: Sentence):
    # random seed with sentence text for reproducibility
    np.random.seed(sum([ord(c) for c in sentence.text]))  
    random_vector = np.random.rand(500)
    random_vector = [float(x) for x in random_vector]
    return random_vector
