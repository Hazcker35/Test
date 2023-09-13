from parse_cookie import parse_cookie

def test_parse_cookie():
	cookie_str = "name=John; age=30; city=New York"
	result = parse_cookie(cookie_str)
	assert result == {'name': 'John', 'age': '30', 'city': 'New York'}

	cookie_str = ""
	result = parse_cookie(cookie_str)
	assert result == {}

	cookie_str = "  name = John ; age = 30  ;  city = New York  "
	result = parse_cookie(cookie_str)
	assert result == {'name': 'John', 'age': '30', 'city': 'New York'}

	cookie_str = "name=John; age=; city=New York"
	result = parse_cookie(cookie_str)
	assert result == {'name': 'John', 'age': '', 'city': 'New York'}

	cookie_str = "name=John; age=30; city= "
	result = parse_cookie(cookie_str)
	assert result == {'name': 'John', 'age': '30', 'city': ''}

	cookie_str = ";;;"
	result = parse_cookie(cookie_str)
	assert result == {}

	cookie_str = "name= ; age= ; city= "
	result = parse_cookie(cookie_str)
	assert result == {'name': '', 'age': '', 'city': ''}

	cookie_str = "=John; age=30; city=New York"
	result = parse_cookie(cookie_str)
	assert result == {'': 'John', 'age': '30', 'city': 'New York'}

	cookie_str = "nameJohn; age=30; city=New York"
	result = parse_cookie(cookie_str)
	assert result == {'age': '30', 'city': 'New York'}

	cookie_str = "John; age=30; city=New York"
	result = parse_cookie(cookie_str)
	assert result == {'age': '30', 'city': 'New York'}