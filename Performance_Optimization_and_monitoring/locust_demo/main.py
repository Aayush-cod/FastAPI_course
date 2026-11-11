from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title = 'LocustFastapi')

class InputData(BaseModel):
    feature1: float
    feature2: float

@app.get('/')
def root():
    return {'message': 'Locust demo'}

@app.post('/predict')
def predict(data : InputData):
    result = data.feature1 + data.feature2
    return {'result': result}