import re

def find_words_starting_with_a(text):
    pass
    pattern = r'\bA\w*'
    return re.findall(pattern,text)

print(find_words_starting_with_a("Alice and Bob met Amy at an Airport."))
print(find_words_starting_with_a("Amazing! An_underscore, A1, and A-B were noted; also an apple."))