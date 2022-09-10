from datetime import datetime


class UserRoleEntity:
    user_id: str
    role_id: str
    role_name: str
    assign_date: datetime
    assign_status: str

    class Meta:
        # Fields to expose
        fields = ("user_id", "role_id", "role_name", "assign_date", "assign_status")

    def __init__(self, user_id: str = None, role_id: str = None, role_name: str = None,
                 assign_date: datetime = None, assign_status: str = None):
        self.user_id = user_id
        self.role_id = role_id
        self.role_name = role_name
        self.assign_date = assign_date
        self.assign_status = assign_status

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "role_id": self.role_id,
            "role_name": self.role_name,
            "assign_date": self.assign_date,
            "assign_status": self.assign_status
        }

    def __eq__(self, other):
        if not isinstance(other, UserRoleEntity):
            return False

        user_eq = self.user_id == other.user_id
        role_eq = self.role_id == other.role_id

        return user_eq and role_eq
