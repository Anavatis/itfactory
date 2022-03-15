from typing import List

from app import db
from models.employee import Employee
from models.store import Store


def get_stores_by_phone(phone_number, count=10) -> List[Store]:
    employee = db.session.query(Employee).get(phone_number)
    if not employee: raise

    return employee.stores
