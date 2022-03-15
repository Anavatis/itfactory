from app import db
from app.error.schemas import ErrorResponseModel
from models.employee import Employee
from models.store import Store


def create_store(name, employees_phone) -> Store:
    if db.session.query(Store).get(name):
        raise ErrorResponseModel(400, "Store already exist")

    employees = [db.session.query(Employee).get(p) for p in employees_phone]

    store = Store(name=name, employees=employees)
    db.session.add(store)
    db.session.commit(store)

    return store


def add_employees(store_name, employees_phone):
    store = get_store(store_name)
    employees = [db.session.query(Employee).get(p) for p in employees_phone]
    store.employees += employees

    db.session.add(store)
    db.session.commit()

    return store


def remove_employees(store_name, employees_phone):
    store = get_store(store_name)
    employees = [db.session.query(Employee).get(p) for p in employees_phone]
    store.employees = list(set(store.employees) - set(employees))

    db.session.add(store)
    db.session.commit()

    return store


def delete_store(store_name):
    store = get_store(store_name)
    db.session.delete(store)
    db.session.commit()


def get_store(store_name):
    store = db.session.query(Store).get(store_name)
    if not store:
        raise ErrorResponseModel(400, "Store not exist")
    return store
