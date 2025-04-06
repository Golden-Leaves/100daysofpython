import string
import random
text = "xcbxcbbxbc ⁤‍‍‌⁡‍‌‌⁡‍‍‍⁡⁢⁣⁡⁢‌‍⁣‌⁡⁢‌⁤⁡⁤‍‌‍⁤⁣⁡⁢‌⁡‍‌‍⁢‌‍⁡‍⁢‍⁤⁡‍‍⁣‌‌⁣⁣‌‍⁡‌‍⁢‍⁢‍zdz"
custom_key = "passwordzzz"
def vigenere(message,key,direction = 1):
    key_index = 0
    final_message = ""
    alphabet = "En0Y)-tvUe,iIzTk4Dg2r*[$w<8hc~mN\\'^9A.y}1j{:W\"ZV](#%+/BFxp3l57R!SaJ=ofOsbHuq>;@_Q6GLP?K\\\\X|MC`&d"

    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            key_char = key[key_index  % len(key)]#The message may be longer than the key.
            key_index += 1
            offset = alphabet.index(key_char)
            index = alphabet.find(char)
            new_index = (index + offset * direction) % len(alphabet)#The key character off set + the message offset maybe longer than the alphabet
            final_message += alphabet[new_index]
    return final_message
def encrypt(message,key):
    return vigenere(message,key)
def decrypt(message,key):
    return vigenere(message,key,-1)
if __name__ == "__main__":
    Encrypted = decrypt(text,custom_key)
    print(Encrypted)

    