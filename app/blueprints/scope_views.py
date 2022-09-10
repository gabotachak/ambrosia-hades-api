"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator
from app.schemas.scope_schema import ScopeSchema
from app.utils.constants import PING_RESPONSE

scope_bp = Blueprint("scope", __name__)


@scope_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK


@scope_bp.route("/<string:scope_id>", methods=["GET"])
@error_decorator
def get_scope_by_id(scope_id: str):
    """Get scope info by scope id."""

    res = app.scope_controller.get_scope_by_id(scope_id)
    return jsonify(res), HTTPStatus.OK


@scope_bp.route("/name/<string:scope_name>", methods=["GET"])
@error_decorator
def get_scope_by_name(scope_name: str):
    """Get scope info by scope name."""

    res = app.scope_controller.get_scope_by_name(scope_name)
    return jsonify(res), HTTPStatus.OK


@scope_bp.route("/", methods=["POST"])
@error_decorator
def create_scope():
    """Create new scope."""

    scopes_req = request.get_json(force=True)

    new_scope = ScopeSchema().load(scopes_req)

    res = app.scope_controller.create_scope(new_scope)

    return jsonify(res), HTTPStatus.CREATED
