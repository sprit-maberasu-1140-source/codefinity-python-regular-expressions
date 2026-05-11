import re

def is_strong_password(password: str) -> bool:
    pass
    if len(password) <8 :
        return False
    if not re.search(r"[A-Z]",password):
        return False
    if not re.search(r"[a-z]",password):
        return False
    if not re.search(r"\d",password):
        return False
    if not re.search(r"[^A-Za-z0-9]",password):
        return False
    return True

print(is_strong_password("Abcdef1!"))
print(is_strong_password("weakpass"))