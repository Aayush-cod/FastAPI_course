from fastapi import FastAPI, Depends , HTTPException , Header


app = FastAPI()

API_KEY = 'my_secret_key'

def get_api_key(api_key:str = Header(...)):
    if api_key != API_KEY:
        raise HTTPException(403, detail = 'Invalid Key')
    return api_key


@app.get('/get-data')
def get_data(api_key : str = Depends(get_api_key)):
    return {'access':'granted'}