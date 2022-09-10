"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE, SCOPES

user_scope_bp = Blueprint("user_scope", __name__)


@user_scope_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""

    return jsonify(PING_RESPONSE), HTTPStatus.OK


@user_scope_bp.route("/<string:user_id>", methods=["GET"])
@error_decorator
def get_user_scopes(user_id: str):
    """Returns every scope assigned to an user by user id"""

    roles = app.user_scope_controller.get_user_scopes(user_id)
    return jsonify({SCOPES: roles}), HTTPStatus.OK
