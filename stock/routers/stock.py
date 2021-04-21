from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models, oauth2
from sqlalchemy.orm import Session
from typing import List 
from ..repository import stock

router = APIRouter(
    prefix="/Stock",
    tags=['Stocks']
)

get_db = database.get_db

# input each route
@router.get('/', response_model=List[schemas.ShowStock])
def all(db : Session =  Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return stock.get_all(db)


# use status to auto create the status codes
@router.post('/', status_code=status.HTTP_201_CREATED)
# converts session into pydantic
def create(request: schemas.Stock, db: Session =  Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return stock.create(request, db)



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return stock.destroy(id, db)

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id: int, request: schemas.Stock, db: Session = Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return stock.update(id, request, db)



@router.get('/{id}', status_code=200, response_model=schemas.ShowStock)
def show(id: int, db: Session =  Depends(get_db), current_user: schemas.User = Depends(oauth2.get_current_user)):
    return stock.show(id, db)

