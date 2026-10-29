from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class user(BaseModel):
    id : int
    name : str


@app.get('/user', response_model = user)
def get_user():
    return user(id = 1, name = 'Aayush')
