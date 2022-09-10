from marshmallow import Schema, fields


class ScopeListSchema(Schema):
    scope_list = fields.List(fields.String())
