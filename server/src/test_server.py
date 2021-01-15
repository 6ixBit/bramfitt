import unittest

from . import app

class TestServerRoutes(unittest.TestCase):
    def test_api_rout(self):
        tester = app.test_client(self)
        res = tester.get("/api", content_type='application/json')
        self.assertEqual(res.status_code, 200)
       
    def test_db_route(self):
        tester = app.test_client(self)
        res = tester.get("/db", content_type='application/json')
        self.assertEqual(res.status_code, 200)

if __name__ == '__main__':
    unittest.main()