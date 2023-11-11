# import unittest
# from app import create_app

# class TestApp(unittest.TestCase):

#     def setUp(self):
#         app = create_app()
#         app.config['TESTING'] = True
#         self.client = app.test_client()

#     def test_index_route(self):
#         response = self.client.get('/')
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Gender Prediction', response.data)

#     def test_predict_route(self):
#         data = {'height': 70, 'weight': 150}
#         response = self.client.post('/predict', data=data)
#         self.assertEqual(response.status_code, 200)
#         self.assertIn(b'Prediction Result', response.data)

# if __name__ == '__main__':
#     unittest.main()
import unittest
from app import create_app
from selenium import webdriver
import pytest

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

@pytest.mark.parametrize("browser", ["chrome", "firefox"])
def test_selenium(browser):
    # Replace with the actual path to your webdriver executable
    webdriver_path = "path/to/your/webdriver/executable"

    with webdriver.Chrome(executable_path=webdriver_path) as driver:
        driver.get("http://localhost:5000")  # Replace with your app's URL
        assert "Gender Prediction" in driver.title

        # Add more Selenium tests as needed
        # ...

if __name__ == '__main__':
    # If you run this file directly, it will run both unit and Selenium tests
    unittest.main()