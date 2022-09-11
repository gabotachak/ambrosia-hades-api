from app.utils.constants import ERROR_RESPONSE
from tests.utils.constants import *

PONG_RESPONSE = {"message": "pong"}

# role_views

ROLE_OK_NO_SCOPES_RESPONSE = {
    "description": "role 1 desc",
    "name": VALID_ROLE_NAME,
    "role_id": VALID_ROLE_ID
}

ROLE_OK_SCOPES_RESPONSE = {
    "description": "role 1 desc",
    "name": VALID_ROLE_NAME,
    "role_id": VALID_ROLE_ID,
    "scopes": [
        VALID_SCOPE_NAME
    ]
}

ROLE_NOT_FOUND_ID_RESPONSE = {
    ERROR_RESPONSE: f'RoleEntity ({VALID_ROLE_ID}) not found'
}

ROLE_NOT_FOUND_NAME_RESPONSE = {
    ERROR_RESPONSE: f'RoleEntity ({VALID_ROLE_NAME}) not found'
}

ROLE_ALREADY_EXISTS_RESPONSE = {
    ERROR_RESPONSE: f'RoleEntity ({VALID_ROLE_NAME}) already exists'
}
