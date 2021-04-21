from pydantic import BaseModel
from typing import List
# if you are using pydantic, you will need to extend BaseModel
class StockBase(BaseModel):
    ticker: str
    description: str

class Stock(StockBase):
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str

class ShowUser(BaseModel):
    name: str
    email: str
    stocks: List[Stock] = []
    # you need to set the ORM mode when using a db.  Otherwise you get a dict error
    class Config():
        orm_mode = True

# extend Stock class
class ShowStock(Stock):
    ticker: str
    description: str
    owner: ShowUser
    # you need to set the ORM mode when using a db.  Otherwise you get a dict error
    class Config():
        orm_mode = True

class Login(BaseModel):
    username: str
    password: str