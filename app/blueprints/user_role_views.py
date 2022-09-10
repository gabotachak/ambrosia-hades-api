"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE, ROLES

user_role_bp = Blueprint("user_role", __name__)


@user_role_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK


@user_role_bp.route("/<string:user_id>", methods=["GET"])
@error_decorator
def get_user_roles(user_id: str):
    """Returns every role assigned to a user"""
    roles = app.user_role_controller.get_user_roles(user_id)
    return jsonify({ROLES: roles}), HTTPStatus.OK
