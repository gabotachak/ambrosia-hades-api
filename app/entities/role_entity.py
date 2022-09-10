class RoleEntity:
    role_id: str
    name: str
    description: str

    class Meta:
        # Fields to expose
        fields = ("role_id", "name", "description")

    def __init__(self, role_id: str = None, name: str = None, description: str = None):
        self.role_id = role_id
        self.name = name.upper()
        self.description = description

    def to_dict(self):
        return {
            "role_id": self.role_id,
            "name": self.name,
            "description": self.description
        }

    def __eq__(self, other):
        if not isinstance(other, RoleEntity):
            return False

        return self.name == other.name
