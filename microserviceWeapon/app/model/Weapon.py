from app import db
from dataclasses import dataclass

@dataclass
class Weapon(db.Model):
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    model = db.Column('model', db.String(100), nullable=False)
    brand = db.Column('brand', db.String(100), nullable=False)
    owner = db.Column('owner', db.Integer,  nullable=False)
    
    def __init__(self, model, brand, owner):
        self.model = model
        self.brand = brand
        self.owner = owner