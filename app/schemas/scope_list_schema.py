from marshmallow import Schema, fields, validate, post_load

from app.utils.constants import SCOPES


class ScopeListSchema(Schema):
    scopes = fields.List(fields.String(required=True, validate=validate.Length(min=4, max=20)), required=True)

    @post_load
    def make_scope_list(self, data, **kwargs):
        return [s.upper() for s in data.get(SCOPES)]
