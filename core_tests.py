import unittest
import json
from app import app, load_quotes

class FlaskAPIRoutesTestCase(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # Load quotes before running the tests
        load_quotes()
        app.testing = True
        cls.client = app.test_client()

    def test_diagnostic_route(self):
        response = self.client.get('/diagnostic')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['status'], 'ok')

    def test_get_quote_route(self):
        response = self.client.get('/api/quote')
        data = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response.status_code, 200)
        self.assertIn('quote', data)

    def test_invalid_route(self):
        response = self.client.get('/invalid')
        self.assertEqual(response.status_code, 404)

if __name__ == '__main__':
    unittest.main()
