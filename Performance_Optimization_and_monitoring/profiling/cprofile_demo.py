import cProfile , time , datetime, os
from fastapi import FastAPI , Request
from fastapi.responses import JSONResponse

app = FastAPI(title='cProfile')

PROFILE_DIR = 'profiles'
os.makedirs(PROFILE_DIR, exist_ok = True)

@app.middleware('http')
async def create_cprofiling(req : Request , call_next):
    time_stamp = datetime.datetime.now().strftime("%m_%d_%Y-%H_%M_%S_%f")
    path = req.url.path.strip('/') or 'root'
    profile_name = os.path.join(PROFILE_DIR, f'{path}_{time_stamp}.prof')

    profiler = cProfile.Profile()
    profiler.enable()

    # callnext now refers to the next handler function. so u can name it in any way - call_next , callnext - mainused is call_next
    response = await call_next(req)

    profiler.disable()
    profiler.dump_stats(profile_name)

    print(f'Profile saved: {profile_name}')
    return response

@app.get('/')
def home():
    return {'message': 'cProfile demo'}


@app.get('/compute')
async def compute():
    time.sleep(1)
    result = sum((i * 2) for i in range(10000))
    return JSONResponse({'result': result})
