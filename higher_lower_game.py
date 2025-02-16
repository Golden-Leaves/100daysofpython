import random
from higher_lower_game_data import *
def check_answer(celebrity_A,celebrity_B):
    if celebrity_A["followers"] > celebrity_B["followers"]:
        return "a"
    else:
        return "b"
    
def game(celebrity_A,celebrity_B,player_input,score):
    is_correct = check_answer(celebrity_A,celebrity_B)
    if player_input == is_correct:
        print(f"{celebrity_A["name"]}'s follower count is : {celebrity_A["followers"]:,}; {celebrity_B["name"]}'s follower count is {celebrity_B["followers"]:,}.")
        score += 1
        print(f"You're right!, your current score is {score}")
        return True,score
    else:
        print(f"You're wrong!, your final score is {score}")
        print(f"{celebrity_A["name"]}'s follower count is : {celebrity_A["followers"]:,}; {celebrity_B["name"]}'s follower count is {celebrity_B["followers"]:,}.")
        return False,score

def main():
    celebrity_A = random.choice(instagram_celebrities_followers_count)
    celebrity_B = random.choice(instagram_celebrities_followers_count)
    score = 0
    while celebrity_A == celebrity_B:#Safeguard in case both are equal
        celebrity_A = random.choice(instagram_celebrities_followers_count)
        celebrity_B = random.choice(instagram_celebrities_followers_count)
    invalid_input_counter = 0
    while invalid_input_counter != 3 :
      celebrity_A_followers = celebrity_A["followers"]
      celebrity_B_followers = celebrity_B["followers"]
      print(f"A: {celebrity_A["name"]}, {celebrity_A["description"]}, from {celebrity_A["country"]}")
      print("\n" + VS_ascii_art)
      print(f"B: {celebrity_B["name"]}, {celebrity_B["description"]}, from {celebrity_B["country"]}")
      player_input = input("Who has more followers on Instagram? 'a' for A, 'b' for B: ").lower()
      if player_input != 'a' and player_input != 'b':
        print("Please enter a valid input.")
        invalid_input_counter += 1
        print(f"Entering invalid inputs 3 times counts as a game over: Current invalid counts {invalid_input_counter}")
      else:
        correct,score = game(celebrity_A,celebrity_B,player_input,score)#Returned value is a tuple
        if correct :
            celebrity_A = celebrity_B
            celebrity_B = random.choice(instagram_celebrities_followers_count)
            while celebrity_A == celebrity_B:
              celebrity_B = random.choice(instagram_celebrities_followers_count)
        else:
            return
          
if __name__ == "__main__":
    main()
