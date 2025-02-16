import string
def vigenere(text,key,direction = 1):
    uppercase_alphabet = string.ascii_uppercase
    lowercase_alphabet = string.ascii_lowercase
    numbers = string.digits
    output = ""
    current_index = 0
    offset = 0
    key_index = 0
    current_index_status = ""


    for character in text:
        
        if not character.isalnum():
            output += character
        else:
            key_char = key[key_index % len(key)]
            key_index += 1
            if key_char.isupper():
                offset = uppercase_alphabet.index(key_char) % len(uppercase_alphabet)

            elif key_char.islower():
                offset = lowercase_alphabet.index(key_char) % len(lowercase_alphabet)

            elif key_char.isdigit():
                offset = numbers.index(key_char) % len(numbers)

                
            if character.isupper():
                current_index = uppercase_alphabet.index(character) % len(uppercase_alphabet)
                new_index = (current_index + offset) * direction % len(uppercase_alphabet)
                new_char = uppercase_alphabet[new_index]

            elif character.islower():
                current_index = lowercase_alphabet.index(character) % len(lowercase_alphabet)
                new_index = (current_index + offset) * direction % len(lowercase_alphabet)
                new_char = lowercase_alphabet[new_index]

            elif character.isdigit():
                current_index = numbers.index(character) % len(numbers)
                new_index = (current_index + offset) * direction % len(numbers)
                new_char  = numbers[new_index]
            output += new_char
            
    def encrypt(text,key):
        vigenere(text,key,direction = 1)
    def decrypt(text,key):
        vigenere(text,key,direction = -1)
    

            


            

if __name__ == "__main__":
    vigenere("132g1br3b","python")