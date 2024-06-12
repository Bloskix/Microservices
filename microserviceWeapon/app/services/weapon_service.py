from app.model import Weapon
from app.repositories.weapon_repository import WeaponRepository
from app import cache
import requests

class WeaponService:
    def __init__(self):
        self.__repo = WeaponRepository()

    def create(self, entity: Weapon) -> Weapon:
        print(entity.owner)
        response = requests.get(f'https://microserviceclient.microservicio.localhost/api/v1/findById/{entity.owner}')
        if response.status_code != 200:
            raise ValueError('Owner does not exist')
        else:
            weapon = self.__repo.create(entity)
            cache.set(f'weapon_{weapon.id}', weapon, timeout=50)
            return weapon

    def find_all(self) -> list:
        return self.__repo.find_all()
    
    def find_by_id(self, id: int) -> Weapon:
        weapon = cache.get(f'weapon_{id}')
        if not weapon:
            weapon = self.__repo.find_by_id(id)
            cache.set(f'weapon_{id}', weapon, timeout=50)
        return weapon
    
    def delete(self, id: int) -> None:
        cache.delete(f'weapon_{id}')
        return self.__repo.delete(id)