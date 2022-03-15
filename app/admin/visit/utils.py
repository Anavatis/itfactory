from sqlalchemy import desc

from app import db
from models.employee import Employee
from models.store import Visit


def get_visits(employee_name, store_name, count=100, offset=0):
    query = (db.session.get(Visit)
             .limit(count)
             .offset(offset)
             .order_by(desc(Visit.visited_on)))

    if store_name:
        query.filter_by(store_name=store_name)

    if employee_name:
        employees = db.session.query(
            Employee).filter_by(name=employee_name).all()
        employees_phone = [e.phone_number for e in employees]
        query.filter(Visit.employee_phone.in_(employees_phone))

    return query.all()