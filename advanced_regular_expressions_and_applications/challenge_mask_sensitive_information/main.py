import re

def mask_credit_card_numbers(text):
    def mask_match(match):
        number = match.group()
        # スペースやハイフンを外して数字だけを数える
        digits = re.sub(r"[ -]", "", number)
        if len(digits) != 16:
            return number  # 16桁じゃなかったら元のまま
        masked = []
        digit_count = 0
        # 後ろから１文字ずつ見ていく
        for c in number[::-1]:
            if c.isdigit():
                digit_count += 1
                # 後ろから5番目より前なら「*」、そうでなければ数字をそのまま
                if digit_count > 4:
                    masked.append('*')
                else:
                    masked.append(c)
            else:
                # ハイフンやスペースはそのまま
                masked.append(c)
        # 逆向きに直して完成
        return ''.join(masked[::-1])

    # 4つずつ区切られた16桁の数字を探す
    pattern = r'((?:\d{4}[- ]?){3}\d{4})'
    return re.sub(pattern, mask_match, text)

print(mask_credit_card_numbers("Pay with 4111 1111 1111 1111 or 5500-0000-0000-0004 today."))
print(mask_credit_card_numbers("Card: 1234-5678-9012-3456; Backup: 4444 3333 2222 1111."))