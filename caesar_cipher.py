import string
alphabet = string.ascii_lowercase
def caesar_cipher(message,shift,direction = 1):
    final_message = ""
    for char in message.lower():
        if not char.isalpha():
            final_message += char
        else:
            message_char = alphabet.index(char)
            new_char = alphabet[(message_char + shift * direction)  % len(alphabet)]
            final_message += new_char
    print(f"Your final message is {final_message}")
    return final_message

def encryption(message,shift):
    return caesar_cipher(message,shift,direction = 1)
def decryption(message,shift):
    return caesar_cipher(message,shift,direction = -1)
def main():

    while True:
      try:
        message = input("Enter your text: ")
        encryption_or_decryption = input("Enter 'e' for encrypt, and 'd' for decrypt: ").lower()
        char_shift = int(input("How many characters to shift by: "))
        if encryption_or_decryption == "e":
            encryption(message,char_shift)
            continue
        elif encryption_or_decryption == "d":
            decryption(message,char_shift)
            continue
        else:
            print("Invalid input.")
            continue
      except ValueError:
          print("Invalid input.")
if __name__ == "__main__":
    main()