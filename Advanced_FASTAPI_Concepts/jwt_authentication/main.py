from fastapi import FastAPI , HTTPException , Depends
from fastapi.security import OAuth2PasswordBearer , OAuth2PasswordRequestForm
from utils import get_user, verify_password
from auth import create_access_token, verify_token

app = FastAPI()

Oauth = OAuth2PasswordBearer(tokenUrl = 'token')

@app.post('/token')
def login(form_data : OAuth2PasswordRequestForm = Depends()):
    user = get_user(form_data.username)
    if not user:
        raise HTTPException(400, detail='Invalid credentials')
    if not verify_password(form_data.password, user['hashed_password']):
        raise HTTPException(400, detail='Invalid password')

    access_token = create_access_token(data = {'sub': form_data.username})
    return {'access_token': access_token , 'token_type':'bearer'}


@app.get('/users')
def read_users(token : str = Depends(Oauth)):
    username = verify_token(token)
    return {'username': username}


