from alphabet import *

encryption_map = {element: index for index, element in enumerate(alphabet)}

def normalise(word: str) -> str:
    result_str = ""
    for char in word:
        if char == ' ':
            continue
        if char.isalpha():
            char = char.upper()
        result_str += char
    return result_str

def gen_new_alphabet(aux_key: str) -> str:
    normalised_key = normalise(aux_key)
    new_alphabet = list(alphabet)
    for i in range(len(normalised_key) - 1, -1, -1):
        new_alphabet.remove(normalised_key[i])
        new_alphabet = [normalised_key[i]] + new_alphabet
    return new_alphabet