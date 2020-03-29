"""
This web service should support the following operations:
○ Add new employee.
○ Remove an employee.
○ Search employees by different filters (at least 2 filters).
○ Get the top 5 of employees with the lowest salaries.

uvicorn e8:app --reload
"""
from fastapi import FastAPI
from pydantic import BaseModel
from e1 import Employee
from datetime import date
from copy import deepcopy


app = FastAPI()
employee_stack = []


class EmployeeItem(BaseModel):
    name: str
    lastname: str
    age: str
    address: str

    employee_code: int
    salary_per_hour: float
    position: str
    department: str
    start_date: date
    

@app.get('/employees/search/by_age/{age}')
def search_by_age(age: int):
    match = [a.json_repr() for a in employee_stack if a.age == age]
    return {'requested': match}


@app.get('/employees/search/by_department/{department}')
def search_by_department(department: str):
    match = [a.json_repr() for a in employee_stack if a.department == department]
    return {'requested': match}


@app.get('/employees/search/lower_paid')
async def get_lower_employees():
    stack = deepcopy(employee_stack)
    stack.sort(key=lambda x: x.salary_per_hour)
    lower_paid = [a.json_repr() for a in stack][:5]
    return {'requested': lower_paid}


@app.get("/")
async def read_root():
    return {"instruction": "go to /docs to watch endpoints"}


@app.get("/employees/")
async def list_employees():
    return {'employees': [e.json_repr() for e in employee_stack]}


@app.post("/employee/")
async def create_employee(employeeItem: EmployeeItem):
    new_employee = Employee(
        employeeItem.name,
        employeeItem.lastname,
        employeeItem.age,
        employeeItem.address,
        len([employee_stack]),
        employeeItem.salary_per_hour,
        employeeItem.start_date,
        employeeItem.position,
        employeeItem.department
    )
    employee_stack.append(new_employee)
    return {'created': new_employee.json_repr()}


@app.get("/employee/{item_id}")
async def show_employee(item_id: int):
    requested_employee = [a.json_repr() for a in employee_stack if a.employee_code == item_id]
    return {'requested': requested_employee}


@app.delete("/employee/{item_id}")
async def delete_employee(item_id: int):
    requested_employee = [a.json_repr() for a in employee_stack if a.employee_code == item_id]
    employee_stack.remove(requested_employee)
    return {'deleted': 'ok'}