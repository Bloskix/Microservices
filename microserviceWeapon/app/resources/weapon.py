from flask import Blueprint, jsonify, request
from app.services.weapon_service import WeaponService
from ..mapping.weapon_schema import WeaponSchema
from ..model.response_message import ResponseBuilder
from app.mapping.response_shema import ResponseSchema

service = WeaponService()
weapon_schema_many = WeaponSchema(many=True)
weapon_schema = WeaponSchema()
response_schema = ResponseSchema()
weapon = Blueprint('weapon', __name__)

@weapon.route('/', methods=['GET'])
def index():
    return {'message': 'Welcome to Weapon API'}, 200

@weapon.route('/', methods=['POST'])
def create_weapon():
    response_builder = ResponseBuilder()
    weapon = weapon_schema.load(request.json)
    response_builder.add_message('Weapon created successfully').add_status_code(100).add_data(weapon_schema.dump(service.create(weapon)))
    return response_schema.dump((response_builder.build())), 200

@weapon.route('/all', methods=['GET'])
def find_all_weapons():
    list = service.find_all()
    result = weapon_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp

@weapon.route('/<int:id>', methods=['GET'])
def find_by_id(id): 
    response_builder = ResponseBuilder()
    response = weapon_schema.dump(service.find_by_id(id))
    if response:
        response_builder.add_message('Weapon found').add_status_code(100).add_data(response)
        return response_schema.dump(response_builder.build()), 200
    else:
        response_builder.add_message('Weapon not found').add_status_code(404).add_data(response)
        return response_schema.dump(response_builder.build()), 404
    
@weapon.route('/<int:id>', methods=['DELETE'])
def delete_weapon(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Weapon deleted successfully').add_status_code(200).add_data(weapon_schema.dump(service.delete(id)))
    return response_schema.dump(response_builder.build()), 200
 