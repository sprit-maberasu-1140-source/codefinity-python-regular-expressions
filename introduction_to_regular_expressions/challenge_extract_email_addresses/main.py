import re

def extract_emails(text):
    pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    return re.findall(pattern, text)

print(extract_emails("Contact us at support@example.com or sales@shop.co.uk for details."))
print(extract_emails("Invalid: user@@example.com, correct: hello.world123@mail.io"))