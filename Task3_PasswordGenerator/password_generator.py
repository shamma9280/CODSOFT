import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    password_var.set(password)

def copy_password():
    root.clipboard_clear()
    root.clipboard_append(password_var.get())

# GUI Setup
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x250")

# Label
tk.Label(root, text="Password Length:", font=("Arial", 14)).pack(pady=10)

# Entry
length_entry = tk.Entry(root, font=("Arial", 14))
length_entry.pack()

# Generate Button
tk.Button(root, text="Generate Password", command=generate_password, font=("Arial", 12)).pack(pady=10)

# Display Password
password_var = tk.StringVar()
tk.Entry(root, textvariable=password_var, font=("Arial", 14), width=30).pack()

# Copy Button
tk.Button(root, text="Copy to Clipboard", command=copy_password, font=("Arial", 12)).pack(pady=10)

root.mainloop()
