from marshmallow import Schema, fields, validate


class ScopeListSchema(Schema):
    scopes = fields.List(fields.String(required=True, validate=validate.Length(min=4, max=20)), required=True)
