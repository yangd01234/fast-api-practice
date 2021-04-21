from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from typing import List 
from ..hashing import Hash

router = APIRouter(
    prefix="/user"
    tags=['Users']
)

get_db = database.get_db

# create users
@router.post('/', response_model=schemas.ShowUser)
def create_user(request: schemas.User, db: Session =  Depends(get_db)):
    new_user = models.User(name=request.name, email=request.email, password=Hash.bcrypt(request.password))
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

# get user without password
@router.get('/{id}', response_model=schemas.ShowUser)
def get_user(id: int, db: Session =  Depends(get_db)):
    # NOTE: There is a HUGE delay if you don't put .first()
    user = db.query(models.User).filter(models.User.id == id).first()

    # use response to add a 404 no found status code
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"User with id {id} is not avaialble")
    return user