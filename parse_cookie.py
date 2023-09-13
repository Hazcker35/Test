def parse_cookie(cookie_str):
	cookies = {}
	if not cookie_str:
		return cookies

	cookie_parts = cookie_str.split(';')
	for part in cookie_parts:
		key_value = part.strip().split('=')
		if len(key_value) == 2:
			key, value = key_value[0].strip(), key_value[1].strip()
			cookies[key] = value

	return cookies
