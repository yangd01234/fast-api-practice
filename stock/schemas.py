from pydantic import BaseModel

# if you are using pydantic, you will need to extend BaseModel
class Stock(BaseModel):
    ticker: str
    description: str