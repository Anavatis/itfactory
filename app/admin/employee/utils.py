from app import db
from app.error.schemas import ErrorResponseModel
from models.employee import Employee


def create_new_employee(name, phone_number) -> Employee:

    if db.session.query(Employee).get(phone_number):
        raise ErrorResponseModel(400, "User already exist")

    employee = Employee(name=name, phone_number=phone_number)
    db.session.add(employee)
    db.session.commit(employee)

    return employee


def edit_employee(phone_number, **kwargs) -> Employee:
    employee = db.session.query(Employee).get(phone_number)
    check_existing_employee(employee)

    for k, v in kwargs.items():
        setattr(employee, k, v)

    db.session.add(employee)
    db.session.commit()

    return employee


def delete_employee(phone_number):

    employee = db.session.query(Employee).get(phone_number)
    check_existing_employee(employee)

    db.session.delete(employee)
    db.session.commit()


def check_existing_employee(employee):
    if not employee:
        raise ErrorResponseModel(400, "User not exist")








