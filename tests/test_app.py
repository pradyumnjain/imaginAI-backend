# test_app.py
import json
import unittest

from app.main import app


class TestApp(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()

    def test_get_data(self):
        response = self.app.get("/api/data")
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "GET request successful")

    def test_post_data(self):
        payload = {"key": "value"}
        response = self.app.post(
            "/api/data", json=payload, content_type="application/json"
        )
        data = json.loads(response.get_data(as_text=True))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data["message"], "POST request successful")
        self.assertEqual(data["data"], payload)


if __name__ == "__main__":
    unittest.main()
