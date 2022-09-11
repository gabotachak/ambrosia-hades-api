from app.utils.constants import ERROR_RESPONSE, SCOPES
from tests.utils.constants import *

PONG_RESPONSE = {"message": "pong"}

# Scope Views

SCOPES_OK_RESPONSE = [
    VALID_SCOPE_NAME
]

# Role Views

ROLE_OK_NO_SCOPES_RESPONSE = {
    "description": "role 1 desc",
    "name": VALID_ROLE_NAME,
    "role_id": VALID_ROLE_ID
}

ROLE_OK_SCOPES_RESPONSE = {
    "description": "role 1 desc",
    "name": VALID_ROLE_NAME,
    "role_id": VALID_ROLE_ID,
    "scopes": SCOPES_OK_RESPONSE
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

# RoleScope Views

ROLE_SCOPES_OK_RESPONSE = {
    SCOPES: SCOPES_OK_RESPONSE
}

ROLE_SCOPES_NOT_FOUND_NAME_RESPONSE = {
    ERROR_RESPONSE: f'RoleScopeEntity ({VALID_ROLE_NAME}) not found'
}