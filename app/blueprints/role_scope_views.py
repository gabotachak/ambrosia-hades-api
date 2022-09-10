"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

import app
from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

role_scope_bp = Blueprint("role_scope", __name__)


@role_scope_bp.route("/ping", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK


@role_scope_bp.route("/<string:role_id>", methods=["GET"])
@error_decorator
def get_role_scopes_by_id(role_id: str):
    """Returns every scope assigned to a role"""
    scopes = app.role_scope_controller.get_role_scopes_by_id(role_id)
    return jsonify({"scopes": scopes}), HTTPStatus.OK


@role_scope_bp.route("/name/<string:role_name>", methods=["GET"])
@error_decorator
def get_role_scopes_by_name(role_name: str):
    """Returns every scope assigned to a role"""
    scopes = app.role_scope_controller.get_role_scopes_by_name(role_name)
    return jsonify({"scopes": scopes}), HTTPStatus.OK
