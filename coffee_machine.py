#Espresso,latte,cappuccino
#Penny = 0.01$, Dime = 0.10$, Nickel = 0.05$, Quarter = 0.25$
profit = 0
def refill_resources(current_resources):
    for item in current_resources:
        if item == "coffee":
            current_resources[item] += 300
            print(f"Refilled {item}g of coffee.")
        elif item == "water":
            current_resources[item] += 200
            print(f"Refilled {item}ml of water.")
        elif item == "milk":
            current_resources[item] += 100
            print(f"Refilled {item}ml of milk.")
    
def is_resources_sufficient(coffee_order,current_resources):
    for item in coffee_order:
        if coffee_order[item] >= current_resources[item]:
            print(f"Sorry, there is not enough {item}")
            current_resources[item] -= coffee_order[item]
            return False
    return True
def process_coins():
    print("Please insert coins.")
    while True:
      try:
        #Value in dollars
        penny_total = int(input("Insert the number of pennies: "))* 0.01
        nickel_total = int(input("Insert the number of nickels: ")) *0.05
        dime_total = int(input("Insert the number of dimes: ")) *0.1
        quarter_total = int(input("Insert the number of quarters: "))* 0.25
        total_money_processed = penny_total + nickel_total + dime_total + quarter_total
        return total_money_processed 
      except ValueError:
        print("Invalid input, please try again.")
        continue
def is_transaction_successful(money_received, drink_cost):
    global profit
    if money_received >= drink_cost:
        change = round(money_received - drink_cost)
        print(f"Here is {change}$ in change.")
        profit += drink_cost
        return True
    elif money_received < drink_cost:
        print(f"{money_received}$ was not enough, refunding money...")
        return False


def main():
    global profit
    menu = {
    "espresso": {
        "water": 50,
        "coffee": 10,
    },
    "latte": {
        "water":200,
        "milk":150,
        "coffee":24,
    },
    "cappucchino":{
        "water":250,
        "milk": 100,
        "coffee":24,
    },
    "money":{
        "espresso": 5,
        "latte":10,
        "cappucchino":15,     
    }
}
    resources = {
        "water": 300,
        "milk": 200,
        "coffee":100,
    }

    is_off = False
    while not is_off:
      print("What would you like?")
      coffee_choice = input("Espresso, latte or cappucchino?: ").lower()
      if coffee_choice == "off":
        is_off = True
        break
      elif coffee_choice == "report":
            print(f"Milk: {resources["milk"]}ml")
            print(f"Water: {resources["water"]}ml")
            print(f"Coffee: {resources["coffee"]}g")
            continue
      try:
        menu_choice = menu[coffee_choice]
        if is_resources_sufficient(menu_choice,resources):
            money_processed = process_coins()
            print(f"You deposited, {money_processed}$")
            if is_transaction_successful(money_processed,menu["money"][coffee_choice]):
                print(f"Transaction successful!. Enjoy your {coffee_choice}!")
      except KeyError:
          print(f"Sorry, {coffee_choice} is not on the menu.")
          continue
    while is_off:
        print("Resources remaining:")
        print(f"Milk: {resources["milk"]}")
        print(f"Water: {resources["water"]}")
        print(f"Coffee: {resources["coffee"]}")
        resources_refil = input("Would you like to refill resources or view the profits? 'y' for yes, 'n' to turn off maintenance mode, 'p' to view profits: ").lower()#Off is the secret word to completely shut down the machine
        if resources_refil == "y":
            refill_resources(resources)
        elif resources_refil == "n":
            is_off = False
            break
        elif resources_refil == "p":
            print(f"Profit accumalated {profit}$")
            continue
        elif resources_refil == "off":
            return True
        else:
            print("Invalid input.")
            continue
        


        
if __name__ == "__main__":
    while True:
      if main():
        break
    