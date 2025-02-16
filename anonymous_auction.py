logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print("\n" * 10)
def compare_money(bidders):
    highest_bid = 0
    winner = ""
    for name in bidders:
        bidders_money = bidders[name]
        if bidders_money > highest_bid:
            highest_bid = bidders_money
            winner = name
        return winner,highest_bid
  

def main():
    bidder_information = {}
    print(logo)
    while True:
      try:
        bidder_name = input("What is your name?: ")
        bidder_payment = int(input("How much do you want to bid?:$"))
        continue_bidding = input("Are there any other bidders? ('y' for yes) ('n' for no): ").lower()
        
        if continue_bidding == 'y':
          bidder_information[bidder_name] = bidder_payment
          compare_money(bidder_information)
          
        elif continue_bidding == 'n':
            bidder_information[bidder_name] = bidder_payment
            value = compare_money(bidder_information)
            print(f"The highest bidder is {value[0]} at {value[1]}") # Winner var comes first in value tuple
            return
        
        else:
            print("Invalid input.")

            
      except ValueError:
        print("Invalid input.")
if __name__ == "__main__":
    main()
    