from morse_code import MORSE_CODE_DICT,REVERSED_MORSE_CODE_DICT
def encrypt_or_decrpt(message,direction=1):#Dir 1 for encode Dir 0 for decode
    final_message = ""
    if direction == 1:
        for char in message:
            morse_character = MORSE_CODE_DICT[char.upper()] + " " 
            final_message += morse_character
    else:
        for morse_word in message.split(" / "):
            for morse_char in morse_word.split(" "):
                character = REVERSED_MORSE_CODE_DICT[morse_char]
                final_message += character
            final_message += " "
    return final_message.rstrip()
if __name__ == "__main__":
    while True:
        try:
            direction = input("Enter 1 to encode, 0 to decode: ")
            if direction not in ("0","1"):
                print("Please enter either 0 or 1.")
                continue
            
            print(encrypt_or_decrpt(input("Input the message to encode/decode: "),int(direction)))
        except KeyError:
            print("Invalid character(s)/morse code detected, please enter valid input.")
            continue
        