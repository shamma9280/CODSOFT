import tkinter as tk
from tkinter import messagebox

contacts = []

def add_contact():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()

    if name and phone:
        contacts.append({"Name": name, "Phone": phone, "Email": email})
        messagebox.showinfo("Success", "Contact added successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
        email_entry.delete(0, tk.END)
        view_contacts()
    else:
        messagebox.showwarning("Input Error", "Name and Phone are required!")

def view_contacts():
    contact_list.delete(0, tk.END)
    for i, contact in enumerate(contacts):
        contact_list.insert(tk.END, f"{i+1}. {contact['Name']} | {contact['Phone']} | {contact['Email']}")

def delete_contact():
    selected = contact_list.curselection()
    if selected:
        index = selected[0]
        contacts.pop(index)
        view_contacts()
        messagebox.showinfo("Deleted", "Contact deleted!")
    else:
        messagebox.showwarning("Select", "Please select a contact to delete.")

# GUI setup
root = tk.Tk()
root.title("Contact Book")
root.geometry("400x500")
root.configure(bg="lightblue")

# Labels and entries
tk.Label(root, text="Contact Book", font=("Arial", 16), bg="lightblue").pack(pady=10)

tk.Label(root, text="Name", bg="lightblue").pack()
name_entry = tk.Entry(root, width=30)
name_entry.pack()

tk.Label(root, text="Phone", bg="lightblue").pack()
phone_entry = tk.Entry(root, width=30)
phone_entry.pack()

tk.Label(root, text="Email", bg="lightblue").pack()
email_entry = tk.Entry(root, width=30)
email_entry.pack()

tk.Button(root, text="Add Contact", command=add_contact).pack(pady=10)
tk.Button(root, text="Delete Selected", command=delete_contact).pack()

tk.Label(root, text="All Contacts", bg="lightblue").pack(pady=5)
contact_list = tk.Listbox(root, width=50)
contact_list.pack()

view_contacts()

root.mainloop()
