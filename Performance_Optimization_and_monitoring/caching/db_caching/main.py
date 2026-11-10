from fastapi import FastAPI
from pydantic import BaseModel
import redis , sqlite3, hashlib , json 


app = FastAPI()

redis_client = redis.Redis(host = 'localhost', port=6379, db = 0 )

def db_connection():
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = db_connection()
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY,
            name TEXT NOT NULL,
            age INTEGER
        )
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO users (id, name, age)
        VALUES (1, 'Aayush', 21)
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO users (id, name, age)
        VALUES (2, 'Atish', 24)
    """)

    cursor.execute("""
        INSERT OR IGNORE INTO users (id, name, age)
        VALUES (3, 'Aakash', 18)
    """)

    conn.commit()
    conn.close()


init_db()


class UserQuery(BaseModel):
    user_id : int


def make_cached_key(user_id : int):
    raw = f'user: {user_id}'
    return hashlib.sha256(raw.encode()).hexdigest()


@app.post('/get_user')
def get_user(user : UserQuery):
    key = make_cached_key(user.user_id)

    cached_data = redis_client.get(key)
    if cached_data:
        print('Fetching user from Redis.....')
        return json.loads(cached_data)

    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users WHERE id = ?", (user.user_id,))
    row = cursor.fetchone()
    conn.close()

    if row is None:
        return {'message': 'User not found.'}

    result = {'id' : row['id'], 'name': row['name'], 'age': row['age']}
    redis_client.setex(key , 3600 , json.dumps(result))
    print('Fetched from DB and Cached!')

    return result

    


