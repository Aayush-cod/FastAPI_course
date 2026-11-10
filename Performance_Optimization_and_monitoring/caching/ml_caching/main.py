from fastapi import FastAPI
from pydantic import BaseModel
import redis , json
import hashlib, joblib


app = FastAPI()

redis_client = redis.Redis(host = 'localhost', port = 6379, db = 0)

model = joblib.load('model.joblib')

class IrisFlower(BaseModel):
    SepalLengthCm: float
    SepalWidthCm: float
    PetalLengthCm: float
    PetalWidthCm: float

    def to_list(self):
        return [
            self.SepalLengthCm,
            self.SepalWidthCm,
            self.PetalLengthCm,
            self.PetalWidthCm
        ]

    def chache_key(self):
        # here self means above irisflower object or pydantic object 
        # model_dump() is a method from pydantic which converts pydantic object to python objetc or dict may be
        raw = json.dumps(self.model_dump(), sort_keys = True)

        return f"predict : {hashlib.sha256(raw.encode()).hexdigest()}"


@app.post('/predict')
async def predict(data : IrisFlower):
    key = data.chache_key()

    cached_result = redis_client.get(key)

    if cached_result:
        print("Returning chached data from redis....")
        return json.loads(cached_result)

    prediction = model.predict([data.to_list()])[0]
    result = {'prediction' : int(prediction)}
    redis_client.set(key , json.dumps(result), ex = 3600)
    return result