#Tommorrow's task, add the condition if the dealer's hand is < 17, then make the dealer take some more cards.
import random
blackjack_game_screen_art = r""".------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _' |/ __| |/ / |/ _' |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
'-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\
      |  \/ K|                            _/ |                
      '------'                           |__/    """
      
card_deck = [2,3,4,5,6,7,8,9,10,10,10,10,"Ace"]
def calculate_score(player,dealer):
    dealer_score = 0
    player_score = 0
    ace_value_dealer = random.choice([1,11])
    if "Ace" in player:
      while True:
        try:
          ace_value_player = int(input("What would you like the score for your ace to be? Type 1 or 11:"))#Determines ace's score
          break
        except ValueError:
          print("Invalid input")
    
    for card in player:
        if card == "Ace":
            player_score += ace_value_player
        elif card != "Ace":
            player_score += card
    for card in dealer:
        if card == "Ace":
            dealer_score += ace_value_dealer
        elif card != "Ace":
            dealer_score += card
    return player_score,dealer_score
def is_black_jack(player,dealer):
     player_blackjack =  len(player) == 2 and "Ace" in player and 10 in player
     dealer_blackjack =  len(dealer) == 2 and "Ace" in dealer and 10 in dealer
     if player_blackjack == True and dealer_blackjack == True:
         return "Both"
     elif player_blackjack == True:
         return "Player"
     elif dealer_blackjack == True:
         return "Dealer"

     
def game():
      print(blackjack_game_screen_art)
      player_cards = random.sample(card_deck,2)
      dealer_cards = random.sample(card_deck,2)
      is_black_jack_cards = is_black_jack(player_cards,dealer_cards)
      if is_black_jack_cards == "Player": #Blackjack win condition ('Blackjack' is when the first two cards are a 10 and an ace)
          print("You won!")
      elif is_black_jack_cards == "Dealer":
          print("You lost!")      
      elif is_black_jack_cards == "Both":
          pass
      print(f"Your cards: {player_cards}. Dealer's first card: {dealer_cards[0]}")
      while True:
        deal_or_pass = input("'d' to deal, 'p' to pass: ")
        if deal_or_pass == 'd':
            player_cards.append(random.choice(card_deck))
            break
        elif deal_or_pass == "p":
            break
        else:
            print("Invalid input.")
          
        

      score_of_both = calculate_score(player_cards,dealer_cards)
      player_score = score_of_both[0]
      dealer_score  = score_of_both[1]
      print(f"Your final hand is {player_cards}")
      print(f"Dealer's final hand {dealer_cards}")
      if player_score > 21: #Control flow stuff, if bust conditions activate first, then the rest of the conditionals won't run.
          print("You've lost, you busted!")
      elif dealer_score > 21:
          print("You've won, the dealer busted!")
      elif player_score > dealer_score:
          print("You've won!")
      elif dealer_score > player_score:
          print("You've lost!")
      elif player_score == dealer_score:
          print("It's a draw!")
      return





 
        
def main():
    while True:
      start_game = input("Type 'y' to start blackjack, 'n' to close: ").lower()
      if start_game == 'y':
        game()
      elif start_game == 'n':
        return
      else:
        print("Invalid input.")
    

if __name__ == "__main__":
    main()
    