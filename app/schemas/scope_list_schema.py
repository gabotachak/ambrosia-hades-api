from marshmallow import Schema, fields, validate


class ScopeListSchema(Schema):
    scope_list = fields.List(fields.String(required=True, validate=validate.Length(min=4, max=20)))
