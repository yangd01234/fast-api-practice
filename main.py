from fastapi import FastAPI



# create instance of fast api
app = FastAPI()

'''
Create a function for fast api
@app: path operation decorator
.get(): operation
('/'): path
'''
@app.get('/')
def index():
    return {'data':'stocks'}

'''
fast API works top down, so if you put /stock/unlisted after
/stock/{id} it won't work.  This is becasue since {id} is dynamically
populated, it won't reach /stock/unlisted path
'''
@app.get('/stock/unlisted')
def unlisted():
    return {'data': 'unlisted stocks'}

# start the server using uvicorn main:app --reload and go to localhost:8000

'''
Create a dynamic path by using {}
You can define the type by passing the param as id: int

'''
@app.get('/stock/{id}')
def show(id: int):
    return {'data': id}

@app.get('/stock/{id}/notes')
def notes(id):
    return {'data': {'1', '2'}}