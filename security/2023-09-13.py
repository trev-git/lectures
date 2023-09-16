#!/usr/bin/env python3

def encode_vigenere(text: str, key: str) -> str:
    key_as_int = [ord(c) for c in key]
    text_as_int = [ord(c) for c in text]
    cipher_text = ''
    for i in range(len(text_as_int)):
        value = (text_as_int[i] + key_as_int[i % len(key_as_int)]) % 26
        cipher_text += chr(value + 65)
    return cipher_text

key =  "CODECODECODECODECODECODECODECODECODECODECODECODECODECODECODECOD"
text = "I LIKE CODING IN JAVASCRIPT I ALSO LIKE PYTHON I HATE ASSEMBLER"
cipher = ''
for i in range(len(text)):
    cipher += chr((ord(text[i]) + ord(key[i])) % 26)
print(cipher)
