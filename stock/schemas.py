from pydantic import BaseModel

# if you are using pydantic, you will need to extend BaseModel
class Stock(BaseModel):
    ticker: str
    description: str

# extend Stock class
class ShowStock(Stock):
    ticker: str
    description: str
    # you need to set the ORM mode when using a db.  Otherwise you get a dict error
    class Config():
        orm_mode = True

class User(BaseModel):
    name: str
    email: str
    password: str
class ShowUser(BaseModel):
    name: str
    email: str
    # you need to set the ORM mode when using a db.  Otherwise you get a dict error
    class Config():
        orm_mode = True