"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator
from app.schemas.role_schema import RoleSchema
from app.schemas.scope_list_schema import ScopeListSchema
from app.utils.constants import PING_RESPONSE

role_bp = Blueprint("role", __name__)


@role_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK


@role_bp.route("/<string:role_name>", methods=["GET"])
@error_decorator
def get_role_by_name(role_name: str):
    res = app.role_controller.get_role_by_name(role_name)
    return jsonify(res), HTTPStatus.OK


@role_bp.route("/", methods=["POST"])
@error_decorator
def create_role():
    """Create new role."""
    role_req = request.get_json(force=True)
    scopes_req = role_req.pop('scopes', None)

    new_role = RoleSchema().load(role_req)
    if scopes_req is not None:
        ScopeListSchema().load({'scope_list': scopes_req})

    res = app.role_controller.create_role(new_role, scopes_req)

    return jsonify(res), HTTPStatus.CREATED
