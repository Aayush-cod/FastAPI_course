from passlib.context import CryptContext

pwd_context = CryptContext(schemes = 'bcrypt', deprecated = 'auto')

fake_user_db = {
    'sadiesink':{
        'username':'sadiesink',
        'hashed_password': pwd_context.hash('sec')
    }
}


def get_user(username:str):
    user = fake_user_db.get(username)
    return user

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)