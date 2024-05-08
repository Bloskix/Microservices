import unittest
from app import create_app

class TestApp(unittest.TestCase):
    
    def setUp(self):
        self.app = create_app()
        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.app_context.pop()

    def test_app(self):
        self.assertTrue(self.app is not None)

if __name__ == '__main__':
    unittest.main()
