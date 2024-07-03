from app.models import Client
from app.repositories.client_repository import ClientRepository
from app import cache, db
from tenacity import retry, stop_after_attempt, wait_fixed

class ClientService:
    def __init__(self):
        self.__repo = ClientRepository()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_create(self, entity: Client) -> Client:
        return self.__repo.create(entity)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_find_all(self) -> list:
        return self.__repo.find_all()

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_find_by_id(self, id: int) -> Client:
        return self.__repo.find_by_id(id)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_find_by_name(self, name: str) -> list:
        return self.__repo.find_by_name(name)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_find_by_email(self, email: str) -> Client:
        return self.__repo.find_by_email(email)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_update(self, dto, id: int) -> Client:
        return self.__repo.update(dto, id)

    @retry(stop=stop_after_attempt(3), wait=wait_fixed(2))
    def _repo_delete(self, id: int) -> Client:
        return self.__repo.delete(id)

    # Create
    def create(self, entity: Client) -> Client:
        client = self._repo_create(entity)
        cache.set(f'client_{client.id}', client, timeout=50)
        return client

    # Read
    def find_all(self) -> list:
        clients = cache.get('all_clients')
        if clients is None:
            clients = self._repo_find_all()
            cache.set('all_clients', clients, timeout=50)
        return clients

    def find_by_id(self, id: int) -> Client:
        client = cache.get(f'client_{id}')
        if client is None:
            client = self._repo_find_by_id(id)
        else:
            client = db.session.merge(client)
        cache.set(f'client_{id}', client, timeout=50)
        return client

    def find_by_name(self, name: str) -> list:
        clients = cache.get(f'clients_name_{name}')
        if clients is None:
            clients = self._repo_find_by_name(name)
            cache.set(f'clients_name_{name}', clients, timeout=50)
        return clients

    def find_by_email(self, email: str) -> Client:
        client = cache.get(f'client_{email}')
        if client is None:
            client = self._repo_find_by_email(email)
        else:
            client = db.session.merge(client)
        cache.set(f'client_{email}', client, timeout=50)
        return client

    # Update
    def update(self, dto, id: int) -> Client:
        client = self._repo_update(dto, id)
        cache.set(f'client_{id}', client, timeout=50)
        return client

    # Delete
    def delete(self, id: int) -> Client:
        client = self._repo_delete(id)
        cache.delete(f'client_{id}')
        return client

