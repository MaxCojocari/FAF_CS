from encryption_utils import *

def encrypt(word: str, key: int) -> str:
    tokens = word.upper().split()
    cipher = ''
    for token in tokens:
        for char in token:
            c = (encryption_map[char] + key) % 26
            cipher += alphabet[c]
    return cipher

def encrypt_with_second_key(word: str, key: int, sec_key: str) -> (str, str):
    tokens = word.upper().split()
    cipher = ''
    new_alphabet = gen_new_alphabet(sec_key)
    new_encryption_map = {element: index for index, element in enumerate(new_alphabet)}
    for token in tokens:
        for char in token:
            c = (new_encryption_map[char] + key) % 26
            cipher += new_alphabet[c]
    return ''.join(new_alphabet), cipher

def decrypt(cipher: str, key: int) -> str:
    tokens = cipher.upper().split()
    message = ''
    for token in tokens:
        for char in token:
            m = (encryption_map[char] - key) % 26
            message += alphabet[m]
    return message

def decrypt_with_second_key(cipher: str, key: int, sec_key: str) -> (str, str):
    tokens = cipher.upper().split()
    message = ''
    new_alphabet = gen_new_alphabet(sec_key)
    new_encryption_map = {element: index for index, element in enumerate(new_alphabet)}
    for token in tokens:
        for char in token:
            m = (new_encryption_map[char] - key) % 26
            message += new_alphabet[m]
    return ''.join(new_alphabet), message
