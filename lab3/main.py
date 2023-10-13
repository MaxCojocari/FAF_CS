from playfair import Playfair
from validation import *

def main():
    while True:
        print("Select option: \n0 - encrypt, \n1 - decrypt, \n2 - exit")
        choice = int(input("Your choice: "))
        
        if choice == 0:
            plaintext = input("Give string to encode:\n")
            if not is_valid_input(plaintext):
                continue
            
            key = input("Input the key (in a-z, A-Z range, with length at least 7):\n")
            if not is_valid_key(key):
                continue
            
            p = Playfair(key)
            cipher = p.encrypt(plaintext)

            print(f"Encryption Matrix:")
            p.print_matrix()
            print(f"Encrypted:\n{cipher}")
            print("---------------------------------------------")
            continue

        elif choice == 1:
            cipher = input("Give ciphertext to decrypt:\n")
            if not is_valid_input(cipher):
                continue
            
            key = input("Input the key (in a-z, A-Z range, with length at least 7):\n")
            if not is_valid_key(key):
                continue
            
            p = Playfair(key)
            plaintext = p.decrypt(cipher)

            print(f"Encryption Matrix:")
            p.print_matrix()
            print(f"Decrypted:\n{plaintext}")
            print("---------------------------------------------")
            continue
            
        elif choice == 2:
            return
        
        else:
            print("Wrong choice!")
            print("---------------------------------------------")

if __name__ == '__main__':
    main()