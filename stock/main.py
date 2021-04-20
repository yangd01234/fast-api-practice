from fastapi import FastAPI
from . import schemas, models
from .database import engine


app = FastAPI()

models.Base.metadata.create_all(engine)

@app.post('/stock')
def create(request: schemas.Stock):
    return request