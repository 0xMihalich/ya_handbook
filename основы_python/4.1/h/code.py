def is_palindrome(value):
    if type(value) not in (int, str, tuple, list):
        return False
    elif isinstance(value, int):
        value = str(value)
    elif isinstance(value, str):
        value = value.lower()
    elif isinstance(value, tuple):
        value = list(value)
    return value == value[::-1]
