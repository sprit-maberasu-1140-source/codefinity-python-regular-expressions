import re

def normalize_spaces(text):
    # 2つ以上続くスペースを1つのスペースに置き換える
    return re.sub(r' {2,}', ' ', text)

print(normalize_spaces("Hello   world   !"))  # Hello world !
print(normalize_spaces("A  B    C     D"))  # A B C D