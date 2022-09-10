"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator
from app.schemas.role_schema import RoleSchema
from app.schemas.scope_list_schema import ScopeListSchema
from app.utils.constants import PING_RESPONSE, SCOPES

role_bp = Blueprint("role", __name__)


@role_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""

    return jsonify(PING_RESPONSE), HTTPStatus.OK


@role_bp.route("/<string:role_id>", methods=["GET"])
@error_decorator
def get_role_by_id(role_id: str):
    """Get role info by role id."""

    res = app.role_controller.get_role_by_id(role_id)
    return jsonify(res), HTTPStatus.OK


@role_bp.route("/name/<string:role_name>", methods=["GET"])
@error_decorator
def get_role_by_name(role_name: str):
    """Get role info by role name."""

    res = app.role_controller.get_role_by_name(role_name)
    return jsonify(res), HTTPStatus.OK


@role_bp.route("/", methods=["POST"])
@error_decorator
def create_role():
    """Create new role."""

    role_req = request.get_json(force=True)
    scopes_req = role_req.pop(SCOPES, None)

    if scopes_req is not None:
        scopes_list = ScopeListSchema().load({SCOPES: scopes_req})
    else:
        scopes_list = []

    new_role = RoleSchema().load(role_req)
    res = app.role_controller.create_role(new_role, scopes_list)

    return jsonify(res), HTTPStatus.CREATED
