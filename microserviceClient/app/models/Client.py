from app.config.database import db
from dataclasses import dataclass

@dataclass
class Client(db.Model):
    __tablename__ = 'clients'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column('name', db.String(105))
    dni = db.Column('dni', db.String(9))
    code = db.Column('code', db.String(256))
    address = db.Column('address', db.String(8))
    email = db.Column('email', db.String(105))