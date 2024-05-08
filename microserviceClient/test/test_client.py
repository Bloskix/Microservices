import unittest
from app.models.Client import Client
from app import create_app

class TestClient(unittest.TestCase):

    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()
    
    def test_client(self):
        client = Client(id=1, name='pol', dni='123'
                        , code='123', address='123',
                        email='ejemplo@ejemplo.com')
        self.assertEqual(client.id, 1)
        self.assertEqual(client.name, 'pol')
        self.assertEqual(client.dni, '123')
        self.assertEqual(client.code, '123')
        self.assertEqual(client.address, '123')
        self.assertEqual(client.email, 'ejemplo@ejemplo.com')

if __name__ == '__main__':
    unittest.main()
                         