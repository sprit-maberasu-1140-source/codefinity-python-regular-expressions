import re

def split_sentences(paragraph):
    # 「.」「!」「?」のいずれかで区切って、その記号も含めるパターン
    pattern = r'[^.!?]+[.!?]'
    # 段落全体からパターンに当てはまる部分を全部見つける
    matches = re.findall(pattern, paragraph, re.DOTALL)
    # 前後のいらない空白を消してリストで返す
    return [sentence.strip() for sentence in matches]

print(split_sentences("Hello world. How are you? I'm fine!"))
print(split_sentences("First sentence across " + 
                      "multiple lines! Second one."))