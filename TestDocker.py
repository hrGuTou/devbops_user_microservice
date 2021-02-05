import unittest
import requests

class TestDocker(unittest.TestCase):

    def test_1(self):
        headers = {
            "content_type": "application/json"
        }
        req = {
            "Username": "test",
            "Password": "test"
        }
        rv = requests.post('http://127.0.0.1:4040/login', json=req, headers=headers)

        assert rv.status_code == 200

if __name__ == '__main__':
    unittest.main()