from datetime import datetime


class RoleScopeEntity:
    role_id: str
    role_name: str
    scope_id: str
    scope_name: str
    assign_date: datetime
    assign_status: str

    class Meta:
        # Fields to expose
        fields = ("role_id", "role_name", "scope_id", "scope_name", "assign_date", "assign_status")

    def __init__(self, role_id: str = None, role_name: str = None,
                 scope_id: str = None, scope_name: str = None,
                 assign_date: datetime = None, assign_status: str = None):
        self.role_id = role_id
        self.role_name = role_name
        self.scope_id = scope_id
        self.scope_name = scope_name
        self.assign_date = assign_date
        self.assign_status = assign_status

    def to_dict(self):
        return {
            "role_id": self.role_id,
            "role_name": self.role_name,
            "scope_id": self.scope_id,
            "scope_name": self.scope_name,
            "assign_date": self.assign_date,
            "assign_status": self.assign_status
        }

    def __eq__(self, other):
        if not isinstance(other, RoleScopeEntity):
            return False

        user_eq = self.role_id == other.role_id
        role_eq = self.scope_id == other.scope_id

        return user_eq and role_eq
