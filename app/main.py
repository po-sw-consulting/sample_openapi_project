from fastapi import FastAPI
from app.utils.validator import Validator
app = FastAPI()

@app.get("/")
def read_root():
    rv = "World"
    if Validator.validate(True):
        rv = "World!!!"
    return {"Hello": rv}