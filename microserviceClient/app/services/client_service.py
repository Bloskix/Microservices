from app.models import Client
from app.repositories.client_repository import ClientRepository


class ClientService:
    def __init__(self):
        self.__repo = ClientRepository()

    #Create
    def create(self, entity: Client) -> Client:
        return self.__repo.create(entity)
        
    #Read
    def find_all(self) -> Client:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> Client:
        return self.__repo.find_by_id(id)

    def find_by_name(self, name) -> list:
        return self.__repo.find_by_name(name)
    
    def find_by_email(self, email) -> Client:
        return self.__repo.find_by_email(email)
    
    #Update
    def update(self, dto, id: int) -> Client:
        return self.__repo.update(dto, id)
    
    #Delete
    def delete(self, id: int) -> Client:
        return self.__repo.delete(id)