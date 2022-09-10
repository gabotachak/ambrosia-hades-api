"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator
from app.schemas.list_string_schema import ListStringSchema
from app.schemas.role_schema import RoleSchema
from app.schemas.scope_schema import ScopeSchema
from app.utils.constants import PING_RESPONSE

scope_bp = Blueprint("scope", __name__)


@scope_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK


@scope_bp.route("/", methods=["POST"])
@error_decorator
def create_scope():
    """Create new scope."""
    scope_req = request.get_json(force=True)

    new_scope = ScopeSchema().load(scope_req)

    res = app.scope_controller.create_scope(new_scope)

    return jsonify(res), HTTPStatus.CREATED
