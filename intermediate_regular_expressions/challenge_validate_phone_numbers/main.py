import re

def is_valid_phone_number(phone):
    pattern = r"^\d{3}-\d{3}-\d{4}$"
    return bool(re.match(pattern, phone))

# テストしてみよう
print(is_valid_phone_number("123-456-7890"))  # True
print(is_valid_phone_number("1234567890"))    # False
print(is_valid_phone_number("123-45-6789"))   # False
print(is_valid_phone_number("abc-def-ghij"))  # False