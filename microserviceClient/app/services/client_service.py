from app.models import Client
from app.repositories.client_repository import ClientRepository
from app import cache


class ClientService:
    def __init__(self):
        self.__repo = ClientRepository()

    #Create
    def create(self, entity: Client) -> Client:
        client = self.__repo.create(entity)
        cache.set(f'client_{client.id}', client, timeout=50)
        return client

        
    #Read
    def find_all(self) -> Client:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> Client:
        client = cache.get(f'client_{id}')
        if client is None:
            client = self.__repo.find_by_id(id)
            cache.set(f'client_{id}', client, timeout=50)
        return client

    def find_by_name(self, name) -> list:
        return self.__repo.find_by_name(name)
    
    def find_by_email(self, email) -> Client:
        client = cache.get(f'client_{email}')
        if client is None:
            client = self.__repo.find_by_email(email)
            cache.set(f'client_{email}', client, timeout=50)
        return client
    
    #Update
    def update(self, dto, id: int) -> Client:
        return self.__repo.update(dto, id)
    
    #Delete
    def delete(self, id: int) -> Client:
        return self.__repo.delete(id)