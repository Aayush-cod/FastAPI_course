from fastapi import FastAPI , HTTPException
from CRUD_Validation.model_val import Employee
from typing import List


employee_db : List[Employee] = []

app = FastAPI()


@app.post('/add_employee', response_model = Employee)
def add_employee(new_emp : Employee):
    for employee in employee_db:
        if employee.id == new_emp.id:
            raise HTTPException(status_code = 400, detail= "Employee already exists!")
    employee_db.append(new_emp)
    return new_emp

@app.get('/get_employee', response_model = List[Employee])
def get_employees():
    return employee_db

@app.get('/get_employee/{emp_id}', response_model = Employee)
def get_employee(emp_id : int):
    for index , employee in enumerate(employee_db):
        if employee.id == emp_id:
            return employee_db[index]
    raise HTTPException(status_code = 404, detail="Employee do not found!")

@app.put('/update_employee/{emp_id}', response_model = Employee)
def update_employee(emp_id:int, new_emp: Employee):
    for index , employee in enumerate(employee_db):
        if employee.id == emp_id:
            employee_db[index] = new_emp
            return new_emp
    raise HTTPException(status_code = 404, detail="Employee do not found!")

@app.delete('/del_employee/{emp_id}')
def del_employee(emp_id : int):
    for index , employee in enumerate(employee_db):
            if employee.id == emp_id:
                del employee_db[index]
                return {'message': 'Employee Deleted successfully.'}
    raise HTTPException(status_code = 404, detail="Employee do not found!")
    

    


    
    

    