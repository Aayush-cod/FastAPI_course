from fastapi.testclient import TestClient
from app.main import app


client = TestClient(app)


def test_eligibility_pass():
    payload = {
        'income' : 60000,
        'age': 24,
        'employment_status': 'employeed'
    }

    response = client.post('/loan_eligibility', json=payload)

    assert response.status_code == 200
    assert response.json() == {'eligible': True}

def test_eligibility_fail():
    payload = {
        'income' : 40000,
        'age': 20,
        'employment_status': 'employed'
    }

    response = client.post('/loan_eligibility', json=payload)

    assert response.status_code == 200
    assert response.json() == {'eligible': False}
