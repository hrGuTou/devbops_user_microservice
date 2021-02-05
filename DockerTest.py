import requests
import unittest
import json

class DockerTest(unittest.TestCase):
    def __init__(self):
        self.endpoint = 'localhost:8081'

    def test_1(self):
        req = {
            "Username": "QA_Tester_Dec",
            "Password": "password12345678"
        }

        res = requests.post(self.endpoint+'/login', json=req)
        data = json.loads(res.data.decode('utf-8'))


