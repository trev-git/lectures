text = 'MHILY LZA ZBHL XBPZXBL MVYABUHL HWWPBZ JSHBKPBZ JHLJBZ KPJABT HYJHUBT LZA ULBAYVU'

res = ''

for ch in text:
    if ch == ' ':
        res += ch
        continue

    res += chr((ord(ch)+6) % 26 + ord('A'))

print(res)