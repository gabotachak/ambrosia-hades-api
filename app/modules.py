import os
from urllib.parse import urlparse

from dotenv import load_dotenv

from app.controllers.ping_controller import PingController


def create_database_conn():
    load_dotenv()

    db_uri = os.getenv("DB_URI", "")
    parsed_uri = urlparse(db_uri)

    host = parsed_uri.hostname
    port = parsed_uri.port
    schema = parsed_uri.path[1:]
    users = os.getenv("DB_USER", "")
    password = os.getenv("DB_PASSWORD", "")


ping_controller = PingController()
