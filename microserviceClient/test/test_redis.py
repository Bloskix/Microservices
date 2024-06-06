import unittest
import redis

class TestRedisConnection(unittest.TestCase):
    def test_redis_connection(self):
        try:
            r = redis.Redis(host='localhost', port=6379, db=0)
            r.ping()
        except redis.ConnectionError:
            self.fail("No se pudo establecer la conexión con Redis")