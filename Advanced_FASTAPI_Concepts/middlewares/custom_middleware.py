import time
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware


app = FastAPI()

class TimerMiddleware(BaseHTTPMiddleware):

    async def dispatch(self, req : Request, call_next):
        start = time.time()
        response = await call_next(req)
        duration = time.time()- start
        print(f'Request: {req.url.path} completed in {duration:.3f} seconds.')
        return response

app.add_middleware(
    TimerMiddleware
)

@app.get('/custom')
async def custom():

    for _ in range(1000000):
        pass
    return {"message":"Task completed!"}