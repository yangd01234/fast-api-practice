from fastapi import FastAPI
from .database import engine
from .routers import stock, user, authentication
from . import models

app = FastAPI()

models.Base.metadata.create_all(engine)

app.include_router(authentication.router)
app.include_router(stock.router)
app.include_router(user.router)
