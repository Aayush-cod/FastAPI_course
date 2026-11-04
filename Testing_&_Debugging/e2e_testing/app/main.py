from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Employee(BaseModel):
    income : float
    age : int
    employment_status : str


@app.post('/loan_eligibility')
def user_eligible(employee : Employee):
    if (employee.income >= 50000) and (employee.age >= 21) and (employee.employment_status == 'employeed'):
        return {'eligible': True}
    else :
        return {'eligible': False}