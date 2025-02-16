a = 12
def calculate_tip(money,percentage,people):
    bill_with_tip = round((money + (money / 100 * percentage)) / people, 2)
    print(f"Each person should pay {bill_with_tip}$")
while True:
  try:
    total_amount_of_money = int(input("Enter the total amount of money: $"))
    tip_percentage = int(input("How much would you like to tip?: %"))
    people_present = int(input("How many people are you splitting the bill with?: "))
    calculate_tip(total_amount_of_money,tip_percentage,people_present)
    
  except ValueError:
    print("Invalid input")