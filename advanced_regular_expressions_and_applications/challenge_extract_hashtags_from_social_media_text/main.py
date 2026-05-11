import re

def extract_hashtags(text):
    pattern = r'(?<!\w)#\w+'
    return re.findall(pattern, text)

# テスト
print(extract_hashtags("Excited for the #Python3_12 release! #coding #AI #100DaysOfCode"))
# 出力: ['#Python3_12', '#coding', '#AI', '#100DaysOfCode']