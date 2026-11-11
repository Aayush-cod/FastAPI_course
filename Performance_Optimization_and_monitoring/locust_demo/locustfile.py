
from locust import HttpUser , task , between


class APIUser(HttpUser):
    wait_time = between(1,2)

    @task
    def call_predict(self):
        payload = {
            'feature1' : 1.0,
            'feature2' : 2.0,
        }
        
        self.client.post('/predict', json=payload)

    # (1) is just weightigh meaning above task and below atsk have same weight
    @task(1)
    def call_root(self):
        self.client.get('/')