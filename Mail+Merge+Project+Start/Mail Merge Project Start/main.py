#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp\
import os
print(os.getcwd())
def main():
    pass
    with open(r"./100daysofpython/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Names/invited_names.txt","r") as f:
        names = [name.strip() for name in f.readlines()]
    print(names)
    with open(r"./100daysofpython/Mail+Merge+Project+Start/Mail Merge Project Start/Input/Letters/starting_letter.txt","r") as f:
        letter = f.read()
    new_letter = []
    for name in names:
        n_letter = letter.replace("[name]",name)
        new_letter.append(n_letter)


    with open(r"./100daysofpython/Mail+Merge+Project+Start/Mail Merge Project Start/Output/ReadyToSend/example.txt","w") as f:
        for letter in new_letter:
            f.write(letter +" \n")
      

    
if __name__ == "__main__":
    main()