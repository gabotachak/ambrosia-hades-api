"""Module with ping endpoint."""
from http import HTTPStatus

from flask import Blueprint, jsonify

from app.decorators import error_decorator
from app.utils.constants import PING_RESPONSE

bp_ping = Blueprint("ping", __name__)


@bp_ping.route("/", methods=["GET"])
@error_decorator
def ping_pong():
    """Ping endpoint, used to know if the app is up."""
    return jsonify(PING_RESPONSE), HTTPStatus.OK
