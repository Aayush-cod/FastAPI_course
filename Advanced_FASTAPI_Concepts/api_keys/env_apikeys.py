from fastapi import FastAPI, Depends , HTTPException, Header
from pydantic_settings import BaseSettings, SettingsConfigDict



class Settings(BaseSettings):
    api_key: str

    # Past one
    # class config:
    #     env_file = '.env'

    # lastest
    model_config = SettingsConfigDict(
        env_file = '.env'
    )

settings = Settings()
app = FastAPI()

def get_api_key(api_key: str = Header(...)):
    if api_key != settings.api_key:
        raise HTTPException(403, detail = 'Invalid Key')
    return api_key


@app.get('/get-data')
def get_data(api_key : str = Depends(get_api_key)):
    return {'access':'granted'}