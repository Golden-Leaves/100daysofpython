from tkinter import *
from tkinter import messagebox
import pyperclip
import os
import string
import random
import json
def main():
    window = Tk()
    window.title("Password Manager")
    window.config(padx = 50, pady = 50)
    lock_img = PhotoImage(file = r"100daysofpython/lock_image.png")
    lock_image = Canvas(width = 200, height = 200, highlightthickness = 0 )
    lock_image.create_image(100,100,image = lock_img)
    lock_image.grid(column = 1,row = 0)
    
    def find_password():
        try:
            with open(r"password_manager.json", "r") as f:
                data = json.load(f)
                website_name = website_input.get().lower()
                website_information = data[website_name]
                print(website_information)
                messagebox.showinfo(title = website_name,message = f"Email/Username: {website_information["email_username"]}\nPassword: {website_information["password"]}")
        except FileNotFoundError:
            messagebox.showerror(title = "Oops",message = "No data file found, try entering some information first!")
        except KeyError:
            messagebox.showerror(title  = "Oops",message = "No details for the website exists (check for any typos?)")
    
    def save_information():
        website_name = website_input.get().lower()
        email_username = email_username_input.get()
        password = password_input.get()

        if len(website_name) == 0 or len(password) == 0 or len(email_username) == 0:
            messagebox.showerror(title = "Oops",message = "Make sure to fill out all the fields!")
        else:
            is_ok = messagebox.askokcancel(title = "Confirm Information",message = f"""These are the info entered: \nWebsite: {website_name
    }\nEmail/Username: {email_username}\n Password: {password} \nContinue?""")

            if is_ok:
                new_data = {
                website_name:{
                    "email_username":email_username,
                    "password": password,
                }
            }
                pyperclip.copy(password)
                website_input.delete(0,END)
                password_input.delete(0,END)
                if os.path.exists(r"password_manager.json"):  # Check if file exists
                    with open(r"password_manager.json", "r") as f:
                        #Loads existing data
                        data = json.load(f)
                        #Updates the data dictionary
                        data.update(new_data)
                        print("Done!")
                    with open(r"password_manager.json", "w") as f:
                        #Updates data
                        json.dump(data,f,indent = 4)

                else:  # File doesn't already exist
                    with open(r"password_manager.json", "w") as f:
                        json.dump(new_data,f)
                        print("Done!")



                
    def generate_password():
        full_alphabet = string.ascii_letters
        numbers = string.digits
        allowed_symbols = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

        full_symbols = full_alphabet + numbers + allowed_symbols

        
        random_characters = []
        for character in range(12):
            random_characters.append(random.choice(full_symbols))
        generated_password = "".join(random_characters)
        print(generated_password)
        password_input.delete(0,END)
        password_input.insert(0, string = generated_password)
        
    website_input = Entry(width = 35)
    website_input.grid(column = 1,row = 1,columnspan = 2)
    website_input.insert(0, string = "websitenamexyz")
    
    website_label = Label(text = "Website/Application")
    website_label.grid(column = 0,row = 1)
    
    
    email_username_label = Label(text = "Email/Username")
    email_username_label.grid(column = 0,row = 2)
    
    password_label = Label(text = "Password")
    password_label.grid(column = 0,row = 3)
  
    email_username_input = Entry(width = 35)
    email_username_input.grid(column = 1,row = 2,columnspan = 2 )
    email_username_input.insert(END, string = "name@xyzmail.com")
    
    password_input = Entry(width = 25)
    password_input.grid(column = 1,row = 3)
    
    generate_password_button = Button(text = "Generate Password",command =  generate_password)
    generate_password_button.grid(column = 2,row = 3,columnspan = 2,sticky = "ew")
    
    search_button = Button(text = "Search",width = 10,command = find_password)
    search_button.grid(column = 2,row = 1)
    
    add_information_button = Button(width = 36,text = "Add",command = save_information)
    add_information_button.grid(column = 1,row = 4,columnspan = 2)
    window.mainloop()
    
if __name__ == "__main__":
    main()