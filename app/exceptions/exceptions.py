class ResourceNotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class UserRoleNotFound(ResourceNotFoundException):
    def __init__(self, user_id: str = None, role_id: str = None):
        self.resource = "UserRoleEntity"
        self.resource_id = f"user_id: {user_id}, role_id: {role_id}"


class ResourceAlreadyExistsException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class RoleAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, name: str = None):
        self.resource = "RoleEntity"
        self.resource_id = name


class ScopeAlreadyExistsException(ResourceAlreadyExistsException):
    def __init__(self, name: str = None):
        self.resource = "ScopeEntity"
        self.resource_id = name
