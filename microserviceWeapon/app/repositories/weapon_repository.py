from app.model import Weapon
from app import db 
from .CRUD import Create, Read, Delete

class WeaponRepository(Create, Read, Delete):

    def __init__(self):
        self.model = Weapon
        
    def create(self, dto: Weapon):
        db.session.add(dto)
        db.session.commit()
        return dto
    
    def find_all(self):
        return db.session.query(self.__model).all()
    
    def find_by_id(self, id):
        return db.session.query(self.__model).filter(self.__model.id == id).one()
    
    def delete(self, id):
        entity = self.find_by_id(id)
        db.session.delete(entity)
        db.session.commit()