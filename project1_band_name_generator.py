def create_placeholder():
    with open(r"temp.txt", "w") as f:
        f.write("")
def main():
  while True:
    try:
        with open(r"temp.txt", "r") as f:
            temp_data = f.readline()
            if temp_data == "" or temp_data == " ":
                name_input = input("Enter your name : ")
                with open(r"temp.txt", "w") as f:
                    written_name = f.write(name_input)
                    print(f"Your username is now {name_input}")
            else:
                print(f"Welcome {temp_data}")
    except FileNotFoundError as file:
        create_placeholder()

if __name__ == "__main__":
    main()