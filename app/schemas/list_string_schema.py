from marshmallow import Schema, fields


class ListStringSchema(Schema):
    list_string = fields.List(fields.String())
