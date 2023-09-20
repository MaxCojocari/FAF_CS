from caesar_cipher import *
from validation import *

def main():
    while True:
        print("Select option: \n0 - encrypt, \n1 - decrypt, \n2 - exit")
        choice = int(input("Your choice: "))
        
        if choice == 0:
            input_word = input("Give string to encode:\n")
            if not is_valid_input(input_word):
                continue
            
            key = int(input("Input the key (between 1 and 25 inclusevly):\n"))
            if not is_valid_key(key):
                continue

            sec_key_choice = input("Do you have secondary key? [Y/n]: ")
            if sec_key_choice in ['Y', 'y']:
                sec_key = input("Input the key (with length at least 7):\n")
                if not is_valid_sec_key(sec_key):
                    continue
                (new_alphabet, cipher) = encrypt_with_second_key(input_word, key, sec_key)
                print(f"New alphabet:\n{new_alphabet}")
                print(f"Encrypted string:\n{cipher}")
            elif sec_key_choice in ['N', 'n']:            
                print(f"Encrypted string:\n{encrypt(input_word, key)}")
            else:
                print("Wrong choice!")
            
            print("---------------------------------------------")
            continue

        elif choice == 1:
            input_cipher = input("Give ciphertext to decrypt:\n")
            if not is_valid_input(input_cipher):
                continue
            
            key = int(input("Input the key (between 1 and 25):\n"))
            if not is_valid_key(key):
                continue
            
            sec_key_choice = input("Do you have secondary key? [Y/n]: ")
            if sec_key_choice in ['Y', 'y']:
                sec_key = input("Input the key (with length at least 7):\n")
                if not is_valid_sec_key(sec_key):
                    continue
                (new_alphabet, plaintext) = decrypt_with_second_key(input_cipher, key, sec_key)
                print(f"New alphabet:\n{new_alphabet}")
                print(f"Decrypted:\n{plaintext}")
            elif sec_key_choice in ['N', 'n']:            
                print(f"Decrypted:\n{decrypt(input_cipher, key)}")
            else:
                print("Wrong choice!")
            
            print("---------------------------------------------")
            continue
            
        elif choice == 2:
            return
        else:
            print("Wrong choice!")
            print("---------------------------------------------")

if __name__ == '__main__':
    main()