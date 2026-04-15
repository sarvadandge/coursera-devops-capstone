import unittest
from app import app

class TestAccounts(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_create(self):
        res = self.client.post("/accounts", json={"name": "test"})
        self.assertEqual(res.status_code, 201)

if __name__ == "__main__":
    unittest.main()
