'''
Start the server: uvicorn main:app --reload and go to localhost:8000
Check the docs with swagger: go to url localhost:8000/docs
'''



from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel
import uvicorn


# create instance of fast api
app = FastAPI()

'''
Create a function for fast api
@app: path operation decorator
.get(): operation
('/'): path

You can use pydantic to set the types of params as well.  
Optional = optional otherwise default None

'''
@app.get('/stock')
def index(limit=10, public: bool = True, sort: Optional[str] = None):
    # return max 10 stocks if listed
    if public:
            return {'data':f'{limit} public stocks'}
    else:
        return {'data': f'{limit} private non-ipo stocks'}

'''
fast API works top down, so if you put /stock/unlisted after
/stock/{id} it won't work.  This is becasue since {id} is dynamically
populated, it won't reach /stock/unlisted path
'''
@app.get('/stock/private')
def private():
    return {'data': 'private stocks'}

'''
Create a dynamic path by using {}
You can define the type by passing the param as id: int

'''
@app.get('/stock/{id}')
def show(id: int):
    return {'data': id}

'''
Fastapi will know if you are using a path param or query param
'''
@app.get('/stock/{id}/notes')
def notes(id, limit=10):
    return {'data': {'1', '2'}}

'''
Here we created a basic Stock model
You can use the swagger docs to test your models
'''
class Stock(BaseModel):
    ticker: str
    description: str
    date_ipo: Optional[bool]

'''
Basic route to create a stock
'''
@app.post('/stock')
def create_stock(request: Stock):
    return {'data': f'Created stock with ticker {request.ticker}'}

# create a main to run app using main.py in terminal instead of uvicorn command
# if __name__ == "__main__":
#     uvicorn.run(app, host="127.0.0.1", port=9000)