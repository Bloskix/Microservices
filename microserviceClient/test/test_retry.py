import unittest
from unittest.mock import patch, call
from app.services.client_service import ClientService
from app.models import Client
from tenacity import RetryError

class TestRetryPattern(unittest.TestCase):
    
    @patch('app.repositories.client_repository.ClientRepository.find_by_id')
    def test_retry_pattern(self, mock_find_by_id):
        def side_effect_func(*args, **kwargs):
            exceptions = [Exception("Temporary failure"), Exception("Temporary failure"), Client(id=1, name="Test Client")]
            for exception in exceptions[:-1]:
                print(f"Excepción capturada: {exception}")
                yield exception
            yield exceptions[-1]
        mock_find_by_id.side_effect = side_effect_func()
        service = ClientService()
        result = service._repo_find_by_id(1)
        self.assertIsInstance(result, Client)
        self.assertEqual(mock_find_by_id.call_count, 3)

    @patch('app.repositories.client_repository.ClientRepository.find_by_id')
    def test_retry_pattern_failure(self, mock_find_by_id):
        mock_find_by_id.side_effect = Exception("Permanent failure")
        service = ClientService()
        with self.assertRaises(RetryError):
            service._repo_find_by_id(1)
        self.assertEqual(mock_find_by_id.call_count, 3)

if __name__ == '__main__':
    unittest.main()