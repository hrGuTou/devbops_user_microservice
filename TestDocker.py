import unittest
import requests

class TestDocker(unittest.TestCase):
    def __init__(self):
        self.url = 'localhost:8081'

    def test_1(self):
        req = {
            "Username": "test",
            "Password": "test"
        }
        rv = requests.post('/login', json=req)

        assert rv.status_code == 202

if __name__ == '__main__':
    TestDocker.run()