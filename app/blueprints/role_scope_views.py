"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify, request

import app
from app.decorators import error_decorator
from app.schemas.scope_list_schema import ScopeListSchema
from app.utils.constants import PING_RESPONSE, SCOPES

role_scope_bp = Blueprint("role_scope", __name__)


@role_scope_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""

    return jsonify(PING_RESPONSE), HTTPStatus.OK


@role_scope_bp.route("/<string:role_id>", methods=["GET"])
@error_decorator
def get_role_scopes_by_id(role_id: str):
    """Returns every scope assigned to a role by role id"""

    scopes = app.role_scope_controller.get_role_scopes_by_id(role_id)
    return jsonify({SCOPES: scopes}), HTTPStatus.OK


@role_scope_bp.route("/name/<string:role_name>", methods=["GET"])
@error_decorator
def get_role_scopes_by_name(role_name: str):
    """Returns every scope assigned to a role by role name"""

    scopes = app.role_scope_controller.get_role_scopes_by_name(role_name)
    return jsonify({SCOPES: scopes}), HTTPStatus.OK


@role_scope_bp.route("/<string:role_id>", methods=["POST"])
@error_decorator
def add_scopes_to_role_by_id(role_id: str):
    """Add a scope list to a role by role id"""

    scopes_req = request.get_json(force=True)
    scopes_list = ScopeListSchema().load(scopes_req)

    res = app.role_scope_controller.add_scopes_to_role_by_id(role_id, scopes_list)
    return jsonify(res), HTTPStatus.OK


@role_scope_bp.route("/name/<string:role_name>", methods=["POST"])
@error_decorator
def add_scopes_to_role_by_name(role_name: str):
    """Add a scope list to a role by role name"""

    scopes_req = request.get_json(force=True)
    scopes_list = ScopeListSchema().load(scopes_req)

    res = app.role_scope_controller.add_scopes_to_role_by_name(role_name, scopes_list)
    return jsonify(res), HTTPStatus.OK


@role_scope_bp.route("/<string:role_id>", methods=["PUT"])
@error_decorator
def set_scope_in_role_by_id(role_id: str):
    """Set a scope list in a role by role id"""

    scopes_req = request.get_json(force=True)
    scopes_list = ScopeListSchema().load(scopes_req)

    res = app.role_scope_controller.set_scopes_in_role_by_id(role_id, scopes_list)
    return jsonify(res), HTTPStatus.OK


@role_scope_bp.route("/name/<string:role_name>", methods=["PUT"])
@error_decorator
def set_scope_in_role_by_name(role_name: str):
    """Set a scope list in a role by role name"""

    scopes_req = request.get_json(force=True)
    scopes_list = ScopeListSchema().load(scopes_req)

    res = app.role_scope_controller.set_scopes_in_role_by_name(role_name, scopes_list)
    return jsonify(res), HTTPStatus.OK
