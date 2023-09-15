from alphabet import alphabet

def is_valid_char(char: str) -> bool:
    if char.upper() not in alphabet:
        print(f"You have entered char outside the range: '{char}' ")
        print("Allowed range A-Z, a-z.")
        print("---------------------------------------------")
        return False
    return True

def is_valid_key(key: int):
    valid = 0 < key and key < 26
    if not valid:
        print(f"Incorect key: {key}")
        print("Acceptable range between 1 and 25 inclusively.")
        print("---------------------------------------------")
        return False
    return True

def is_valid_sec_key(sec_key: int):
    tokens = sec_key.upper().split()
    if not tokens:
        print("You entered only blank symbol(s).\nTry again.")
        print("---------------------------------------------")
        return False
    
    normalized_key = ''.join(tokens)
    
    if len(normalized_key) < 7:
        print(f"Invalid key length: {len(normalized_key)}\nTry again.")
        print("---------------------------------------------")
        return False
    
    for token in tokens:
        for char in token:
            if not char in alphabet: 
                print(f"Your secondary key has foreign symbol: '{char}' ")
                print("Allowed range A-Z, a-z.")
                print("---------------------------------------------")
                return False
    return True
            

def is_valid_input(word: str):
    tokens = word.upper().split()
    if not tokens:
        print("You entered only blank symbol(s).\nTry again.")
        print("---------------------------------------------")
        return False
    for token in tokens:
        for char in token:
            if not is_valid_char(char): 
                return False
    return True