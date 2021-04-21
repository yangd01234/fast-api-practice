from fastapi import APIRouter, Depends, status, HTTPException
from .. import schemas, database, models
from sqlalchemy.orm import Session
from typing import List 

router = APIRouter(
    prefix="/Stock",
    tags=['Stocks']
)

get_db = database.get_db

# input each route
@router.get('/', response_model=List[schemas.ShowStock])
def all(db : Session =  Depends(get_db)):
    stocks = db.query(models.Stock).all()
    return stocks


# use status to auto create the status codes
@router.post('/', status_code=status.HTTP_201_CREATED)
# converts session into pydantic
def create(request: schemas.Stock, db: Session =  Depends(get_db)):
    new_stock = models.Stock(ticker=request.ticker, description=request.description, user_id=1) # user id hard coded as 1 for now

    # add and commit new stock using the prior model
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock



@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id, db: Session = Depends(get_db)):
    stock = db.query(models.Stock).filter(models.Stock.id == id)
    if not stock.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with id {id} not found")
    stock.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def update(id, request: schemas.Stock, db: Session = Depends(get_db)):
    stock = db.query(models.Stock).filter(models.Stock.id == id)
    if not stock.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with id {id} not found")
    # note the dict(), forces a dictionary type
    stock.update(dict(request))
    db.commit()
    return 'updated'



@router.get('/{id}', status_code=200, response_model=schemas.ShowStock)
def show(id, db: Session =  Depends(get_db)):
    # NOTE: There is a HUGE delay if you don't put .first()
    stock = db.query(models.Stock).filter(models.Stock.id == id).first()

    # use response to add a 404 no found status code
    if not stock:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id {id} is not avaialble")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"stock with id {id} is not avaialble"}
    return stock

