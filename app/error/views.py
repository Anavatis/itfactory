from flask import Blueprint, jsonify

from app.error.schemas import ErrorResponseModel

error = Blueprint("error", __name__)


@error.app_errorhandler(ErrorResponseModel)
def handle_response_error(e):
    response = jsonify({"error": e.to_dict()})
    response.status_code = e.code
    return response
