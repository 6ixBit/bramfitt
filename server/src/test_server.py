import unittest

from .controller import parse_time, fetch_bus_times

class TestServer(unittest.TestCase):
    def test_parse_time_is_valid(self):
        actual = parse_time("2018-01-02T22:08:12.510696")
        expected = "22:08:12"
        self.assertEqual(actual, expected)

    def test_fetch_bus_times(self):
        actual = fetch_bus_times()
        self.assertEqual(type(actual), list)

if __name__ == '__main__':
    unittest.main()