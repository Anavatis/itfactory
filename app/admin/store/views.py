from flask import Blueprint, request, jsonify

from app import db
from app.admin.store.utils import create_store, remove_employees, add_employees, get_store, delete_store
from app.admin.utils import admin_required
from app.error.schemas import ErrorResponseModel
from models.store import Store

admin_store = Blueprint("admin_store", __name__, url_prefix="/admin/store")


@admin_store.route('/')
@admin_required
def get():
    store_name = request.args.get('name')
    if not store_name:
        raise ErrorResponseModel(400, "Incorrect data")

    store = get_store(store_name)

    return jsonify({"result": store.to_dict()})


@admin_store.route('/', methods=['POST'])
@admin_required
def create():
    store_name = request.args.get('name')
    employees_phone = request.args.get('employees_phone')
    if not store_name:
        raise ErrorResponseModel(400, "Incorrect data")

    store = create_store(store_name, employees_phone)
    return jsonify({"result": store.to_dict()})


@admin_store.route('/add_employee', methods=['PATCH'])
@admin_required
def add_emp():
    store_name = request.args.get('name')
    employees_phone = request.args.get('employees_phone')

    if not store_name:
        raise ErrorResponseModel(400, "Incorrect data")

    store = add_employees(store_name, employees_phone)
    return jsonify({"result": store.to_dict()})


@admin_store.route('/remove_employee', methods=['PATCH'])
@admin_required
def remove_emp():
    store_name = request.args.get('name')
    employees_phone = request.args.get('employees_phone')

    if not store_name:
        raise ErrorResponseModel(400, "Incorrect data")

    store = remove_employees(store_name, employees_phone)
    return jsonify({"result": store.to_dict()})


@admin_store.route('/remove_employee', methods=['DELETE'])
@admin_required
def delete():
    store_name = request.args.get("name")
    if not store_name:
        raise ErrorResponseModel(400, "Incorrect data")

    delete_store(store_name)

    return jsonify({"result": "successful"})