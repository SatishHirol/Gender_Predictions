import unittest
from app import create_app

class TestApp(unittest.TestCase):

    def setUp(self):
        app = create_app()
        app.config['TESTING'] = True
        self.client = app.test_client()

    def test_index_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Gender Prediction', response.data)

    def test_predict_route(self):
        data = {'height': 70, 'weight': 150}
        response = self.client.post('/predict', data=data)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Prediction Result', response.data)

if __name__ == '__main__':
    unittest.main()