from fastapi import FastAPI
from schemas import InputSchema, OutputSchema
from predict import make_prediction, make_batch_predictions
from typing import List

app = FastAPI()


@app.get('/')
def index():
    return {'message': 'Welcome to the ML Model Prediction API'}


@app.post('/prediction', response_model=OutputSchema)
def predict(user_input: InputSchema):
    prediction = make_prediction(user_input.model_dump())
    return OutputSchema(predicted_price=round(prediction, 2))

# @app.post('/prediction', response_model=OutputSchema)
# def predict(user_input: InputSchema):
#     prediction = make_prediction(user_input.model_dump())

#     return {"predicted_price": round(float(prediction), 2)} 
# 
# U have to return OutputSchema object as response model is Output Schema / so u must wrap it like above as only float is coming from model prediction so u have to convert it into object of output schema
    


@app.post('/batch_prediction', response_model=List[OutputSchema])
def batch_predict(user_inputs: List[InputSchema]):
    predictions = make_batch_predictions([x.model_dump() for x in user_inputs])
    return [OutputSchema(predicted_price=round(prediction, 2)) for prediction in predictions]