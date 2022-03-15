from flask import Blueprint, request, jsonify

from app.admin.utils import admin_required
from app.admin.visit.utils import get_visits

admin_visit = Blueprint("admin_visit", __name__, url_prefix="/admin/visit")


@admin_visit.route('/')
@admin_required
def get():

    count = request.args.get('count')
    offset = request.args.get('offset')
    employee_name = request.args.get('employee_name')
    store_name = request.args.get('store_name')

    visits = get_visits(count, offset, employee_name, store_name)
    return jsonify({'result': visits.to_dict()})
