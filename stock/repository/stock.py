from sqlalchemy.orm import Session
from .. import models, schemas
from fastapi import HTTPException, status


def get_all(db: Session):
    stocks = db.query(models.Stock).all()
    return stocks

def create(request: schemas.Stock, db: Session):
    new_stock = models.Stock(ticker=request.ticker, description=request.description, user_id=1) # user id hard coded as 1 for now

    # add and commit new stock using the prior model
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

def destroy(id: int, db: Session):
    stock = db.query(models.Stock).filter(models.Stock.id == id)
    if not stock.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with id {id} not found")
    stock.delete(synchronize_session=False)
    db.commit()
    return 'deleted'

def update(id: int, request: schemas.Stock, db: Session):
    stock = db.query(models.Stock).filter(models.Stock.id == id)
    if not stock.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stock with id {id} not found")
    # note the dict(), forces a dictionary type
    stock.update(dict(request))
    db.commit()
    return 'updated'

def show(id: int, db: Session):
    # NOTE: There is a HUGE delay if you don't put .first()
    stock = db.query(models.Stock).filter(models.Stock.id == id).first()

    # use response to add a 404 no found status code
    if not stock:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"stock with id {id} is not avaialble")
        # response.status_code = status.HTTP_404_NOT_FOUND
        # return {'detail': f"stock with id {id} is not avaialble"}
    return stock
