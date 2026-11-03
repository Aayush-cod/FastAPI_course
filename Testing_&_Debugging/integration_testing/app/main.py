from fastapi import FastAPI
from pydantic import BaseModel
from app.logic import is_eligible_for_loan

app = FastAPI()

class Employee(BaseModel):
    income : float
    age : int
    employment_status : str


@app.post('/loan_eligibility')
def user_eligible(employee : Employee):
    eligibility = is_eligible_for_loan(
        income = employee.income,
        age = employee.age,
        employment_status = employee.employment_status
    )

    return {'eligible': eligibility}