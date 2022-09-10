class ScopeEntity:
    scope_id: str
    name: str
    description: str

    class Meta:
        # Fields to expose
        fields = ("scope_id", "name", "description")

    def __init__(self, scope_id: str = None, name: str = None, description: str = None):
        self.scope_id = scope_id
        self.name = name.upper()
        self.description = description

    def to_dict(self):
        return {
            "scope_id": self.scope_id,
            "name": self.name,
            "description": self.description
        }

    def __eq__(self, other):
        if not isinstance(other, ScopeEntity):
            return False

        return self.name == other.name
