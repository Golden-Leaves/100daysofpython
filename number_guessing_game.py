import random
def game(number,difficulty):
    if difficulty == 'e':
        lives = 10
    elif difficulty == 'h':
        lives = 5
    else:
        print("You've chosen an invalid difficulty!")
        return
    right_number = random.randint(1,100)
    if lives == 0:
        print(f"You've lost! The answer was {right_number}")
        return
    if number > right_number:
        print("Too high.")
        lives -= 1
    elif right_number > number:
        print("Too low.")
        lives -= 1
    elif number == right_number:
        print(f"You've won! the answer was {right_number}")
        return
    print(f"You have {lives} lives left.")
    
def main():
    game_difficulty = input("'e' for easy mode, 'h' for har mode: ")
    while True:
        try:
            user_number = int(input("Guess the number: "))
            game(user_number,game_difficulty)
            break
        except ValueError:
            print("Invalid input")
if __name__ == "__main__":
    while True:
      main()