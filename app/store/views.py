from flask import Blueprint, request, jsonify

from app.store.get import get_stores_by_phone
from app.store.utils import create_visit

store = Blueprint("store", __name__, url_prefix='/store')


@store.route('/', methods=['GET'])
def get_store():
    phone_number = request.args.get('phone')
    count = request.args.get('count', 10)

    if not phone_number: raise

    stores = get_stores_by_phone(phone_number, count)
    store_names = [s.name for s in stores]

    response = jsonify({"result": store_names})
    return response


@store.route('/', methods=['PATCH'])
def visit_store():
    phone_number = request.json.get('phone')
    store_name = request.json.get('store_name')
    latitude = request.json.get('latitude')
    longitude = request.json.get('longitude')

    visit = create_visit(phone_number, store_name, latitude, longitude)
    print(visit)

    return jsonify({"result": visit})





