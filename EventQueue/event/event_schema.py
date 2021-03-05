from marshmallow import Schema, fields

class EventSchema(Schema):
    id = fields.Int(dump_only = True)
    name = fields.Str()
    date = fields.DateTime('%Y-%m-%dT%H:%M:%S+00:00')
    location = fields.Str()
    description = fields.Str()
