import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
from vigenere import vigenere

# --- Password generation function ---
def generate_password(length):
    if length < 4:
        print("Warning: Length too short to ensure character type variety.")
        chars = string.ascii_letters + string.digits
        return "".join(random.choices(chars, k=length))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols),
    ]

    all_chars = lower + upper + digits + symbols
    password += random.choices(all_chars, k=length - 4)
    random.shuffle(password)
    return "".join(password)

# --- Handler for password generation ---
# def handle_generate_password():
#     try:
#         length = int(length_var.get())

#         if length <= 0:
#             messagebox.showerror("Error", "Password length must be a positive number.")
#             return
#         if length > 100:
#             messagebox.showwarning("Warning", "Password length is too long, generation may take time.")

#         generated = generate_password(length)
#         output_entry.config(state='normal')
#         output_entry.delete(0, tk.END)
#         output_entry.insert(0, generated)
#         output_entry.config(state='readonly')
#         status_label.config(text="")

#     except ValueError:
#         messagebox.showerror("Error", "Please enter a valid number.")
#     except Exception as e:
#         messagebox.showerror("Unknown Error", f"An error occurred: {e}")

def handle_encryption_decryption():
        output_entry.config(state='normal')
        output_entry.delete(0, tk.END)
        output_entry.insert(0, vigenere(message=encrypted_password_var.get(),key=key_var.get()))
        output_entry.config(state='readonly')
        status_label.config(text="")
    

# --- GUI setup ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x200")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use('clam')
    root.configure(bg=style.lookup('TFrame', 'background'))

    main_frame = ttk.Frame(root, padding="20 10 20 10")
    main_frame.grid(row=0, column=0, sticky="nsew")

    # Key label & entry
    key_label = ttk.Label(main_frame, text="Key:")
    key_label.grid(row=0, column=0, padx=5, pady=5, sticky="e")

    key_var = tk.StringVar()
    key_entry = ttk.Entry(main_frame, textvariable=key_var, width=10)
    key_entry.grid(row=0, column=1,  pady=5, sticky="w")

    # Length label & entry
    encrypted_password_label = ttk.Label(main_frame, text="Encrypted password:")
    encrypted_password_label.grid(row=0, column=2, padx=5, pady=5, sticky="e")

    encrypted_password_var = tk.StringVar(value="12")
    encrypted_password_entry = ttk.Entry(main_frame, textvariable=encrypted_password_var, width=15)
    encrypted_password_entry.grid(row=0, column=3, padx=5, pady=5, sticky="w")

    # Generate button
    generate_button = ttk.Button(main_frame, text="Decrypt Password", command=handle_encryption_decryption)
    generate_button.grid(row=1, column=0, columnspan=4, pady=10)

    # Output password
    output_label = ttk.Label(main_frame, text="Password:")
    output_label.grid(row=2, column=0, padx=5, pady=5, sticky="e")

    output_entry = ttk.Entry(main_frame, width=30, state='readonly')
    output_entry.grid(row=2, column=1, columnspan=3, padx=5, pady=5, sticky="we")

    # Status label
    status_label = ttk.Label(main_frame, text="")
    status_label.grid(row=3, column=0, columnspan=4, pady=5)

    root.mainloop()
