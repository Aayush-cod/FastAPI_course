from fastapi import FastAPI , Depends

app = FastAPI()


# Dependency function
def get_db():
    db = {'connection':'md_db_connection'}
    try:
        yield db
    finally:
        db.close()




# Dependency Injection
@app.get('/home')
def home(db = Depends(get_db)):
    return {'status':db['connection']}