"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

user_scope_bp = Blueprint("user_scope", __name__)


@user_scope_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK


@user_scope_bp.route("/<string:user_id>", methods=["GET"])
@error_decorator
def get_user_scopes(user_id: str):
    """Returns every role assigned to a user"""
    roles = app.user_scope_controller.get_user_scopes(user_id)
    return jsonify({"scopes": roles}), HTTPStatus.OK
