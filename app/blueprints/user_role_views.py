"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator
from app.schemas.role_list_schema import RoleListSchema
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
    """Returns every role assigned to an user by user id"""

    scopes = app.user_role_controller.get_user_roles(user_id)
    return jsonify({ROLES: scopes}), HTTPStatus.OK


@user_role_bp.route("/<string:user_id>", methods=["POST"])
@error_decorator
def add_roles_to_user(user_id: str):
    """Add a role list to an user by user id"""

    roles_req = request.get_json(force=True)
    roles_list = RoleListSchema().load(roles_req)

    res = app.user_role_controller.add_roles_to_user(user_id, roles_list)
    return jsonify(res), HTTPStatus.OK


@user_role_bp.route("/<string:user_id>", methods=["PUT"])
@error_decorator
def set_role_in_user(user_id: str):
    """Set a role list in an user by user id"""

    roles_req = request.get_json(force=True)
    roles_list = RoleListSchema().load(roles_req)

    res = app.user_role_controller.set_roles_in_user(user_id, roles_list)
    return jsonify(res), HTTPStatus.OK
