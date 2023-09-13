def parse(request_string: str) -> dict:
    """
    Парсит строку HTTP-запроса и возвращает словарь, содержащий поля запроса.

    Args:
      request_string: Строка HTTP-запроса.

    Returns:
      Словарь, содержащий поля запроса.
    """

    request_lines = request_string.split("\n")
    request_line = request_lines[0]
    method, path, _, _ = request_line.split(" ")
    headers = {}

    for header in request_lines[1:]:
        header_name, header_value = header.split(":", 1)
        headers[header_name.strip()] = header_value.strip()

    return {
      "method": method,
      "path": path,
      "headers": headers,
    }


def parse_cookie(cookie_string: str) -> dict:
    """
    Парсит строку, содержащую куки, и возвращает словарь, содержащий поля куки.

    Args:
      cookie_string: Строка, содержащая куки.

    Returns:
      Словарь, содержащий поля куки.
    """

    cookie_dict = {}

    for cookie in cookie_string.split(";"):
        cookie_parts = cookie.strip().split("=", 1)

        if len(cookie_parts) == 2:
            cookie_name, cookie_value = cookie_parts
            cookie_dict[cookie_name] = cookie_value

        elif "httponly" in cookie.lower():
            cookie_dict["httponly"] = True

        elif "secure" in cookie.lower():
            cookie_dict["secure"] = True

    return cookie_dict
