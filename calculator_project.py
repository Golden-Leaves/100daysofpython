import math
calculator_art = """
|  _________________  |
| |                 | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|"""
def arithmetic_functions(input):
    pass
def main():
    print("Welcome to PyCalculator.")
    print(calculator_art)
    while True:
      try:
        user_input = eval(input("Calculate: "))
        print(f"The result is {user_input}")
      except (TypeError, NameError, SyntaxError, ZeroDivisionError):
          print("Please type an appropriate mathematical expression!")
    
if __name__ == "__main__":
    main()