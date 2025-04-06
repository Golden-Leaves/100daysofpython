import tkinter as tk
from tkinter import ttk  # For nicer widgets
from tkinter import messagebox
import random
import string
from vigenere import vigenere
# pyperclip has been removed

# --- Password generation function ---
def generate_password(length):
    """Generate a random password with a specified length."""
    if length < 4:
        print("Warning: Length too short to ensure character type variety.")
        lower = string.ascii_lowercase
        upper = string.ascii_uppercase
        digits = string.digits
        all_chars = lower + upper + digits
        if not all_chars:
            return "Error: No character set available."
        return "".join(random.choices(all_chars, k=length))

    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password = [
        random.choice(lower),
        random.choice(upper),
        random.choice(digits),
        random.choice(symbols)
    ]

    all_chars = lower + upper + digits + symbols

    for _ in range(length - 4):
        password.append(random.choice(all_chars))

    random.shuffle(password)
    return "".join(password)

# --- Button click handler ---
def handle_generate_password():
    try:
        length = int(key_entry.get())

        if length <= 0:
            messagebox.showerror("Error", "Password length must be a positive number.")
            return
        if length > 100:
            messagebox.showwarning("Warning", "Password length is too long, generation may take time.")

        new_password = generate_password(length)

        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(0, new_password)
        password_entry.config(state='readonly')

        status_label.config(text="")

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for length.")
    except Exception as e:
        messagebox.showerror("Unknown Error", f"An error occurred: {e}")

# --- GUI setup ---
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Password Generator")
    root.geometry("400x200")
    root.resizable(False, False)

    style = ttk.Style(root)
    style.theme_use('clam')

    main_frame = ttk.Frame(root, padding="20 10 20 10")
    main_frame.pack(expand=True, fill=tk.BOTH)

    # --- Password length input ---
    key_frame = ttk.Frame(main_frame)
    key_frame.pack(fill=tk.X, pady=5)

    key_label = ttk.Label(key_frame, text="Key:")
    key_label.pack(side=tk.LEFT, padx=5)
    
    password_frame = ttk.Frame(main_frame)
    password_frame.pack(fill=tk.X, pady=5)
    
    password_label = ttk.Label(key_frame, text="Password: ")
    password_label.pack(side=tk.LEFT, padx=5)



    # Key input
    key = tk.StringVar()
    key_entry = ttk.Entry(length_frame, width=5, textvariable=key)
    key_entry.pack(side=tk.LEFT, padx=5) # tiny gap between fields

    # Password input
    password = tk.StringVar()
    password_entry = ttk.Entry(key_frame, width=5, textvariable=password)
    password_entry.pack(side=tk.LEFT,padx=40)


    # --- Generate button ---
    decrypt_button = ttk.Button(main_frame, text="Generate Password", command=handle_generate_password)
    decrypt_button.pack(pady=10)

    # --- Password display ---
    result_frame = ttk.Frame(main_frame)
    result_frame.pack(fill=tk.X, pady=5)

    password_label = ttk.Label(result_frame, text="Password:")
    password_label.pack(side=tk.LEFT, padx=5)

    password_entry = ttk.Entry(result_frame, width=30, state='readonly')
    password_entry.pack(side=tk.LEFT, expand=True, fill=tk.X)

    # --- Status label ---
    status_label = ttk.Label(main_frame, text="")
    status_label.pack(pady=5)

    root.mainloop()
