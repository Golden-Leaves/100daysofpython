import pandas
def main():
 while True:
   print("Welcome to NATO alphabet text converter.")
   nato_alphabet_csv = pandas.read_csv(r"100daysofpython/nato_phonetic_alphabet.csv")
   nato_alphabet = {row.letter:row.code for (index,row) in nato_alphabet_csv.iterrows()}
   user_text = input("Enter text: ").upper().strip()
   if user_text == "EXIT":
       return
   converted_text = [nato_alphabet[letter] for letter in user_text if letter.isalpha()]
   print(", ".join(converted_text))

  

if __name__ == "__main__":
    main()
