from flask import Blueprint, jsonify, request

from app import db
from app.admin.employee.utils import create_new_employee, edit_employee, delete_employee
from app.admin.utils import admin_required
from app.error.schemas import ErrorResponseModel
from models.employee import Employee

admin_employee = Blueprint("admin_employee", __name__, url_prefix="/admin/employee")


@admin_employee.route('/')
@admin_required
def get():
    employee_name = request.args.get("name")
    if not employee_name:
        raise ErrorResponseModel(400, "Incorrect data")

    employee = db.session.query(Employee).get(employee_name)
    if not employee:
        return jsonify({})

    return jsonify({"result": employee.to_dict()})


@admin_employee.route('/', methods=["POST"])
@admin_required
def create():
    phone_number = request.json.get('phone_number')
    name = request.json.get('name')

    if not phone_number or not name:
        raise ErrorResponseModel(400, "Incorrect data")

    employee = create_new_employee(name, phone_number)
    return jsonify({"result": employee.to_dict()})


@admin_employee.route('/', methods=["PATCH"])
@admin_required
def edit():
    phone_number = request.json.pop('phone_number')

    if not phone_number:
        raise ErrorResponseModel(400, "Incorrect data")

    employee = edit_employee(phone_number, **request.json)
    return jsonify({"result": employee.to_dict()})


@admin_employee.route('/', methods=["DELETE"])
@admin_required
def delete():
    phone_number = request.json.get('phone_number')

    if not phone_number:
        raise ErrorResponseModel(400, "Incorrect data")

    delete_employee(phone_number)

    return jsonify({"result": "successful"})
