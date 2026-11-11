from fastapi import FastAPI
from pydantic import BaseModel
import redis , hashlib , json , httpx

app = FastAPI(title = 'Redis Cache')

redis_client = redis.Redis(host = 'localhost', port = 6379 , db = 0)

class PostRequest(BaseModel):
    post_id : int

def make_cached_key(post_id : int):
    raw = f'external_api:post_{post_id}'
    return hashlib.sha256(raw.encode()).hexdigest()


@app.post('/get-data')
async def get_data(post : PostRequest):
    key = make_cached_key(post.post_id)

    cached_data = redis_client.get(key)
    if cached_data:
        print('Fetched from Redis cache.....')
        return json.loads(cached_data)

    print('External API calling ......')
    async with httpx.AsyncClient() as client:
        response = await client.get(f"https://jsonplaceholder.typicode.com/posts/{post.post_id}")
        if response.status_code != 200:
            return {'error': 'Post not found!'}
    # coverts response json into python object
    post_data = response.json()
    redis_client.setex(key , 3600 , json.dumps(post_data))
    print('Fetched and stored in Cache!')
    return post_data