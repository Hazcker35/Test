import unittest
from main import parse_cookie


class TestParseCookie(unittest.TestCase):
    def test_empty_cookie(self):
        cookie_string = ""
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {})

    def test_simple_cookie(self):
        cookie_string = "name=value"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value"})

    def test_cookie_with_expires(self):
        cookie_string = "name=value; expires=Thu, 01 Jan 2023 12:00:00 GMT"
        result = parse_cookie(cookie_string)
        self.assertEqual(result,
                         {
                             "name": "value",
                             "expires": "Thu, 01 Jan 2023 12:00:00 GMT"
                         })

    def test_cookie_with_max_age(self):
        cookie_string = "name=value; max-age=3600"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "max-age": "3600"})

    def test_cookie_with_domain(self):
        cookie_string = "name=value; domain=example.com"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "domain": "example.com"})

    def test_cookie_with_path(self):
        cookie_string = "name=value; path=/"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "path": "/"})

    def test_cookie_with_secure(self):
        cookie_string = "name=value; secure"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "secure": True})

    def test_cookie_with_httponly(self):
        cookie_string = "name=value; httponly"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "httponly": True})

    def test_cookie_with_invalid_expires(self):
        cookie_string = "name=value; expires=INVALID"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "expires": "INVALID"})

    def test_cookie_with_invalid_max_age(self):
        cookie_string = "name=value; max-age=INVALID"
        result = parse_cookie(cookie_string)
        self.assertEqual(result, {"name": "value", "max-age": "INVALID"})
