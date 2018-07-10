import unittest
import pyramid.testing


class HomeControllerTests(unittest.TestCase):

    def setUp(self):
        from pypi import main
        app = main({})
        from webtest import TestApp
        self.app = TestApp(app)

    def test_home_page(self):
        import webtest.response
        response: webtest.response.TestResponse = self.app.get('/', status=200)

        self.assertTrue(b'Find, install and publish Python packages' in response.body)
