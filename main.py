from fastapi import FastAPI



# step 1: create instance of fast api
app = FastAPI()

'''
step 2: create a function for fast api
@app: path operation decorator
.get(): operation
('/'): path
'''
@app.get('/')
def index():
    return 'hello'

# step 3: start the server using uvicorn main:app --reload and go to localhost:8000

# step 4: create another route
@app.get('/about')
def about():
    return {'data':{'about page'}}