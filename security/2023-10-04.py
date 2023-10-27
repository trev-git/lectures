import sys

if len(sys.argv) < 3 or len(sys.argv) > 3:
    print("идинахуй")
    exit(0)

text = sys.argv[1].upper()
shift = int(sys.argv[2])
res = ''

for ch in text:
    if ch == ' ':
        res += ch
        continue
    res += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))

print(res)
