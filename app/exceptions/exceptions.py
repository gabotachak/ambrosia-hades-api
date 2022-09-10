class ResourceNotFoundException(Exception):
    def __init__(self, resource_id, resource=None):
        self.resource = resource
        self.resource_id = resource_id


class RoleNotFoundException(ResourceNotFoundException):
    def __init__(self, role: str = None):
        self.resource = "RoleEntity"
        self.resource_id = role


class ScopeNotFoundException(ResourceNotFoundException):
    def __init__(self, scope: str = None):
        self.resource = "ScopeEntity"
        self.resource_id = scope


class UserRolesNotFoundException(ResourceNotFoundException):
    def __init__(self, user_id: str = None):
        self.resource = "UserRoleEntity"
        self.resource_id = user_id


class RoleScopesNotFoundException(ResourceNotFoundException):
    def __init__(self, role_id: str = None):
        self.resource = "RoleScopeEntity"
        self.resource_id = role_id


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
