import uuid

from marshmallow import Schema, fields, post_load, validate

from app.entities.role_entity import RoleEntity


class RoleSchema(Schema):
    role_id = fields.UUID(load_default=uuid.uuid4)
    name = fields.String(required=True, validate=validate.Length(min=4, max=20))
    description = fields.String(required=True, validate=validate.Length(min=4, max=200))

    @post_load
    def make_role(self, data, **kwargs):
        return RoleEntity(**data)
