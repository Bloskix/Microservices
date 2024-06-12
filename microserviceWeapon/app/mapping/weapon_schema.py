from app.model.Weapon import Weapon
from marshmallow import validate, fields, Schema, post_load

class WeaponSchema(Schema):
    id = fields.Integer(dump_only=True)
    model = fields.String(required=True, validate=validate.Length(min=1))
    brand = fields.String(required=True, validate=validate.Length(min=1))
    owner = fields.Integer(required=True) # La logica de negocio se encargará de validar que el owner exista en la base de datos

    @post_load
    def make_weapon(self, data, **kwargs):
        return Weapon(**data)