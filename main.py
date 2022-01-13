from fastapi import FastAPI

app = FastAPI()

#domain where this api is hosted for example : localhost:5000/docs to see swagger documentation automagically generated.


@app.get("/")
def home():
    return {"message":"Hello World"}


@app.get("/add/")
async def read_item(a: int = 0, b: int = 0):
    return a+b
