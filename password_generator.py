#This shit is archived
import string
import random
alphabet = list(string.ascii_letters)
digits = list(string.digits)
symbols = list(string.punctuation)
password_characters = alphabet + digits + symbols
def generate_password(user_input):
    generated_password = []
    while len(generated_password) < user_input:
        added_character = random.choice(password_characters)
        generated_password.append(added_character)
    generated_password = "".join(generated_password)
    
    print(f"Your generated password is: {generated_password}")

def main():
    print("Welcome to PyPassword Generator...")
    while True:
      try:
        print("Type 'q' to quit")
        character_limit = input("How many characters would you like your password to have?: ")
        if character_limit == "q":
            return
        character_limit = int(character_limit)
        generate_password(character_limit)
        
      except ValueError:
        print("Invalid input, please try again.")
if __name__ == "__main__":
    main()