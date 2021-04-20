from fastapi import FastAPI
from . import schemas


app = FastAPI()



@app.post('/stock')
def create(request: schemas.Stock):
    return request