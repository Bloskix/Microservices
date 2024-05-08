from app.models.Client import Client
from marshmallow import validate, fields, Schema, post_load

"""
Esta clase se encarga de adaptar los modelos a json
"""
class ClientSchema(Schema):
    id = fields.Integer(dump_only=True)
    name = fields.String(required=True, validate=validate.Length(min=1, max=105))
    dni = fields.String(required=True, validate=validate.Length(min=1, max=9))
    email = fields.String(required=True, validate=validate.Length(min=1, max=256))
    code = fields.String(required=True, validate=validate.Length(min=1, max=8))
    address = fields.String(required=True, validate=validate.Length(min=1, max=105))

    @post_load
    def make_user(self, data, **kwargs):
        return Client(**data)