import unittest
from flask import request
from app import create_app, db
from app.models.Client import Client
from app.services.client_service import ClientService

service = ClientService()

class TestClientCRUD(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()
        self.app_context.pop()

    def test_create_client(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        self.assertIsNotNone(entity.id)

    def test_find_all(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        entities = service.find_all()
        self.assertEqual(len(entities), 1)

    def test_find_by_id(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        entity = service.find_by_id(1)
        self.assertEqual(entity.id, 1)

    def test_find_by_name(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        entities = service.find_by_name('Juan')
        self.assertEqual(len(entities), 1)

    def test_find_by_email(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        entity = service.find_by_email('test@cli')
        self.assertEqual(entity.email, 'test@cli')

    def test_update(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        dto = {'name': 'Pedro'}
        service.update(dto, 1)
        entity = service.find_by_id(1)
        self.assertEqual(entity.name, 'Pedro')

    def test_delete(self):
        entity = Client(name='Juan', dni='12345678', code='12345678', address='Calle 12', email='test@cli')
        service.create(entity)
        service.delete(1)
        entity = db.session.query(Client).filter(Client.id == entity.id).first()
        self.assertIsNone(entity)

if __name__ == "__main__":
    unittest.main()