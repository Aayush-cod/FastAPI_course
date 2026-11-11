import time
import logging
from fastapi import FastAPI, Request


app = FastAPI()

logging.basicConfig(
    level = logging.INFO,
    format = "[%(asctime)s] (level - %(levelno)d) - %(levelname)s - %(message)s",
    datefmt = "%m-%d-%Y %H:%M:%S"

)

logger = logging.getLogger('profiling')



@app.middleware('http')
async def get_timing(request : Request, callnext):
    start_time = time.time()
    response = await callnext(request)
    time_taken = time.time() - start_time
    logger.info(f"Request {request.url.path} completed in {time_taken:.3f}s ")
    return response


@app.get('/')
def home():
    return {'message': 'Profiling Demo'}

@app.get('/slow')
async def slow_endpoint():
    time.sleep(2)
    return {'message': 'This is a slow endpoint'}

@app.get('/fast')
async def fast_endpoint():
    return {'message': 'This is a fast endpoint'}