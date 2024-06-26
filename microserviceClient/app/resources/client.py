from flask import Blueprint, jsonify, request
from app.services.client_service import ClientService
from ..mapping.client_schema import ClientSchema
from ..models.response_message import ResponseBuilder
from app.mapping.response_shema import ResponseSchema

service = ClientService() 
client_schema_many = ClientSchema(many=True) # es para que devuelva varios objetos, este se usa para find_all
client_schema = ClientSchema()
response_schema = ResponseSchema()
client = Blueprint('client', __name__)

@client.route('/', methods=['GET'])
def index():
    return {"message":"Welcome to the product API!"}, 200

#Create
@client.route('/create', methods=['POST'])
def create_client():
    response_builder = ResponseBuilder()
    client = client_schema.load(request.json)
    response_builder.add_message("Usuario creado").add_status_code(100).add_data(client_schema.dump(service.create(client)))
    return response_schema.dump((response_builder.build())), 200

#Read
@client.route('/findAll', methods=['GET'])
def find_all_clients():
    list = service.find_all()
    result = client_schema_many.dump(list)
    resp = jsonify(result)
    resp.status_code = 200
    return resp


@client.route('/findById/<int:id>', methods=['GET'])
def find_by_id(id):
    response_builder = ResponseBuilder()
    response = client_schema.dump(service.find_by_id(id))
    if response:
        response_builder.add_message("Usuario encontrado").add_status_code(100).add_data(response)
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder.add_message("No se encontro el usuario").add_status_code(400).add_data(
            response)
        return response_schema.dump((response_builder.build())), 400
    
@client.route('/findByName/<string:name>', methods=['GET'])
def find_by_name():
    name = request.args.get('name')
    response_builder = ResponseBuilder()
    response = client_schema_many.dump(service.find_by_name(name))
    if response:
        response_builder.add_message("Nombre encontrado").add_status_code(100).add_data({'clients': response})
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder.add_message("No se encontro el nombre").add_status_code(400).add_data(
            response)
        return response_schema.dump((response_builder.build())), 400


@client.route('/findByEmail/<string:email>', methods=['GET'])
def find_by_email(email):
    response_builder = ResponseBuilder()
    response = client_schema.dump(service.find_by_email(email))
    if response:
        response_builder.add_message("Email encontrado").add_status_code(100).add_data(
            response)
        # Preguntar si esta bien esta forma, esta forma anda
        return response_schema.dump((response_builder.build())), 200
    else:
        response_builder.add_message("No se encontro el email").add_status_code(400).add_data(
            response)
        return response_schema.dump((response_builder.build())), 400
    
#Update
@client.route('/update/<int:id>', methods=['PUT'])
def update_client(id):
    response_builder = ResponseBuilder()
    client = request.json
    response_builder.add_message("Usuario modificado").add_status_code(100).add_data(client_schema.dump(service.update(client, id)))
    return response_schema.dump((response_builder.build())), 200

#Delete
@client.route('/delete/<int:id>', methods=['DELETE'])
def delete_client(id):
    response_builder = ResponseBuilder()
    response_builder.add_message('Usuario eliminado.').add_status_code(200).add_data(client_schema.dump(service.delete(id)))
    return response_schema.dump(response_builder.build()), 200