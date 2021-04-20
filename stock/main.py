from fastapi import FastAPI, Depends
from . import schemas, models
from .database import engine, SessionLocal
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(engine)

def get_db():
    db = SessionLocal()
    try:
        # THIS IS VERY IMPORTANT.  Yield is a generator.  Make sure to close()
        yield db
    finally:
        db.close()

@app.post('/stock')
# converts session into pydantic
def create(request: schemas.Stock, db : Session =  Depends(get_db)):
    new_stock = models.Stock(ticker=request.ticker, description=request.description)

    # add and commit new stock using the prior model
    db.add(new_stock)
    db.commit()
    db.refresh(new_stock)
    return new_stock

@app.get('/stock')
def all(db : Session =  Depends(get_db)):
    stocks = db.query(models.Stock).all()
    return stocks

@app.get('/stock/{id}')
def show(id, db: Session =  Depends(get_db)):
    # NOTE: There is a HUGE delay if you don't put .first()
    stock = db.query(models.Stock).filter(models.Stock.id == id).first()
    return stock