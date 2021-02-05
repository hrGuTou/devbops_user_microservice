import unittest
import requests

class TestDocker(unittest.TestCase):

    def test_1(self):
        req = {
            "Username": "test",
            "Password": "test"
        }
        rv = requests.post('localhost:8081/login', json=req)

        assert rv.status_code == 202

if __name__ == '__main__':
    unittest.main()