import re

def extract_dates(text):
    # まず、２つの日付の書き方を１つのパターンにまとめます
    # 1) 2025-10-23 のような「年-月-日」
    # 2) 12/05/2024 のような「日/月/年」
    pattern = r"\b(\d{4}-\d{2}-\d{2}|\d{2}/\d{2}/\d{4})\b"
    
    # re.findall は、このパターンに当てはまる部分を全部探してリストで返します
    return re.findall(pattern, text)

print(extract_dates("Important dates: 2025-10-23, 12/05/2024, and 1999-01-01."))
# 出力: ['2025-10-23', '12/05/2024', '1999-01-01']

print(extract_dates("No valid date here, but maybe 31/12/2023 and 2024-07-04 are fine."))
# 出力: ['31/12/2023', '2024-07-04']