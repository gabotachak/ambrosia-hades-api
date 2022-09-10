from datetime import date


class UserRoleEntity:
    class Meta:
        # Fields to expose
        fields = ("user_role_id", "user_id", "role_id", "assign_date", "assign_status")

    def __init__(self, user_role_id: int = None, user_id: str = None, role_id: str = None,
                 assign_date: date = None, assign_status: str = None):
        self.user_role_id = user_role_id
        self.user_id = user_id
        self.role_id = role_id
        self.assign_date = assign_date
        self.assign_status = assign_status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "role_id": self.role_id,
            "assign_date": self.assign_date,
            "assign_status": self.assign_status
        }

    def __eq__(self, other):
        if not isinstance(other, UserRoleEntity):
            return False

        user_eq = self.user_id == other.user_id
        role_eq = self.role_id == other.role_id
        assign_date_eq = self.assign_date = other.assign_date
        assign_status_eq = self.assign_status = other.assign_status

        return user_eq and role_eq and assign_date_eq and assign_status_eq
