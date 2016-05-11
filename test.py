from app import app
import unittest #used to call routes and checking the response data/status code


class FlaskTestCase(unittest.TestCase):

    # Ensure that flask was set up correctly
    def test_index(self):
        tester = app.test_client(self) #test client is used to create a test mocking the functionality of main app. This is an isolated app makes request and test responses from all outside of the scope of main app
        response = tester.get('/login', content_type='html/text') #using the unittest library to call the login route
        self.assertEqual(response.status_code, 200) #checking the status code = 200 or not

    # Ensure that login page works correctly
    def test_login_page_loads(self):
        tester = app.test_client(self)
        response = tester.get('/login', content_type='html/text')
        self.assertTrue(b'Please login' in response.data) #assertTrue cause we are checking text is a part of response or not. checking the data from response contains 'Please login' or not


if __name__ == '__main__':
    unittest.main()
