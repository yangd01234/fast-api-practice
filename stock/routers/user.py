from fastapi import APIRouter, Depends, status
from .. import schemas, database, models
from sqlalchemy.orm import Session
from typing import List 
from ..repository import user

router = APIRouter(
    prefix="/user",
    tags=['Users']
)

get_db = database.get_db

# create users
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session =  Depends(get_db)):
    return user.create_user(request, db)

# get user without password
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session =  Depends(get_db)):
    return user.get_user(id, db)