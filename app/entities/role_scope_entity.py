from datetime import date


class RoleScopeEntity:
    class Meta:
        # Fields to expose
        fields = ("role_scope_id", "role_id", "scope_id", "assign_date", "assign_status")

    def __init__(self, role_scope_id: int = None, role_id: str = None, scope_id: str = None,
                 assign_date: date = None, assign_status: str = None):
        self.role_scope_id = role_scope_id
        self.role_id = role_id
        self.scope_id = scope_id
        self.assign_date = assign_date
        self.assign_status = assign_status

    def to_dict(self):
        return {
            "role_id": self.role_id,
            "scope_id": self.scope_id,
            "assign_date": self.assign_date,
            "assign_status": self.assign_status
        }

    def __eq__(self, other):
        if not isinstance(other, RoleScopeEntity):
            return False

        user_eq = self.role_id == other.role_id
        role_eq = self.scope_id == other.scope_id
        assign_date_eq = self.assign_date = other.assign_date
        assign_status_eq = self.assign_status = other.assign_status

        return user_eq and role_eq and assign_date_eq and assign_status_eq
