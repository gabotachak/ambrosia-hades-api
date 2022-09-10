import uuid

from marshmallow import Schema, fields, post_load, validate

from app.entities.scope_entity import ScopeEntity


class ScopeSchema(Schema):
    scope_id = fields.UUID(load_default=uuid.uuid4)
    name = fields.String(required=True, validate=validate.Length(min=4, max=20))
    description = fields.String(required=True, validate=validate.Length(min=4, max=200))

    @post_load
    def make_scope(self, data, **kwargs):
        return ScopeEntity(**data)
