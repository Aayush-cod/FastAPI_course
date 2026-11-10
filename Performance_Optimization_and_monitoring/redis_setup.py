import redis

r = redis.Redis(host = 'localhost', port = 6379 , db = 0)


try:
    if r.ping():
        print('Connection established with redis..')
except r.exceptions.ConnectionError:
    print('Connection with Redis failed!')


r.set('framework', 'FastAPI')

value = r.get('framework')

print(f"Value from redis :  {value.decode()}")