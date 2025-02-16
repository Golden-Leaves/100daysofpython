import random
def computer_choice():
    valid_actions_list = ["r","p","s"]
    random_choice = random.choice(valid_actions_list)
    return random_choice
def game(computer_choice):
    try:
        rounds = int(input("How many rounds would you like to play? "))
    except ValueError:
        print("Invalid input.")
    current_round = 1
    for round in range(rounds):
        print(f"Current round is {current_round}")
        player_input = input("'r' for rock, 'p' for paper, 's' for scissors: ").lower()


        if player_input == computer_choice:
            print("It's a tie!")
            current_round += 1
        elif player_input == 'r' and computer_choice == 's':
            print("Player won!")
            current_round += 1
        elif player_input == 'r' and computer_choice == 'p':
            print("Computer won!")
            current_round += 1
        elif player_input == 's' and computer_choice == 'p':
            print("Player won!")
            current_round += 1
        elif player_input == 'p' and computer_choice == 'r':
            print("Player won!")
            current_round += 1
        elif player_input == 's' and computer_choice == 'r':
            print("Computer won!")
            current_round += 1
        else:
            print("Invalid input")
        if current_round - 1  == rounds:
            print("Game has ended!")
            return

def main():
    game(computer_choice())
if __name__ == "__main__":
    main()
        



    