import unittest
from main import parse


class TestParse(unittest.TestCase):
    def test_request_with_empty_method(self):
        request_string = "HTTP/1.1\nHost: example.com\n\n"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_empty_path(self):
        request_string = "GET  HTTP/1.1\nHost: example.com\n\n"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_empty_version(self):
        request_string = "GET /index.html \nHost: example.com\n\n"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_multiple_methods(self):
        request_string = "GET POST /index.html HTTP/1.1\nHost: example.com\n\n"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_multiple_paths(self):
        request_string = "GET /index.html /about.html HTTP/1.1\nHost: example.com\n\n"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_multiple_versions(self):
        request_string = "GET /index.html HTTP/1.1 HTTP/2.0\nHost: example.com\n\n"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_invalid_header_name(self):
        request_string = "GET /index.html HTTP/1.1\nHost: example.com\n\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\nInvalid-Header: value"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_invalid_header_value(self):
        request_string = "GET /index.html HTTP/1.1\nHost: example.com\n\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\nInvalid-Header: value "
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_invalid_header_value_too_long(self):
        request_string = "GET /index.html HTTP/1.1\nHost: example.com\n\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\nInvalid-Header: value12345678901234567890123456789012345678901234567890"
        with self.assertRaises(ValueError):
            parse(request_string)

    def test_request_with_invalid_header_value_contains_newline(self):
        request_string = "GET /index.html HTTP/1.1\nHost: example.com\n\nUser-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:82.0) Gecko/20100101 Firefox/82.0\nAccept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8\nInvalid-Header: value\n"
        with self.assertRaises(ValueError):
            parse(request_string)

