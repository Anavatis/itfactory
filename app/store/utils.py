from app import db
from app.error.schemas import ErrorResponseModel
from models.store import Store, Visit


def create_visit(phone_number: str,
                 store_name: str,
                 latitude: float,
                 longitude: float) -> dict:

    store = db.session.query(Store).get(store_name)
    check_phone_linked_to_store(store, phone_number)

    visit = Visit(store_name=store_name,
                  employee_phone=phone_number,
                  latitude=latitude,
                  longitude=longitude)
    db.session.add(visit)
    db.session.commit()

    return {"visit_id": visit.index, "datetime": visit.visited_on.timestamp()}


def check_phone_linked_to_store(store: Store, phone_number: str):
    for employee in store.employees:
        if employee.phone_number == phone_number:
            return

    raise ErrorResponseModel(405, "No access")
