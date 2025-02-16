import random

from hangman_data import *
random_word = random.choice(word_list).lower()
def game(user_input,correct_letters,lives):
    display = ""
    print(f"********** Lives: {lives} **********")
    if user_input not in random_word:#Placing 'lives -= 1' inside the for loop doenst work, unwanted behaviour where it checks every single letter
        print(f"'{user_input}' is not present in the word, you lose 1 life")
        lives -= 1
    elif user_input in correct_letters:
        print(f"You've already guessed {user_input}")

    for letter in random_word:
        if letter == user_input:
            display += user_input
            correct_letters.append(letter)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"
    if "_" not in display:
        return True

    print(display)
    return lives


def main():
    print(random_word)
    placeholder = ""
    for letter in range(len(random_word)):
        placeholder += "_"
    print(placeholder)
    correct_letters_gb = []
    lives_gb = 6
    while lives_gb > 0:
      
      player_input = input("Please type a letter: ").lower()
      hangman_stage_data = hangman_stages_reversed[lives_gb]
      print(hangman_stage_data)
      lives_gb = game(player_input,correct_letters_gb,lives_gb)
      if lives_gb == 0:
          print(hangman_stages_reversed[0])
          print(f"The correct word was {random_word}")
          print("***** YOU LOST *****")
      elif lives_gb == True:
          print("***** YOU WON *****")
          return

if __name__ == "__main__":
    main()