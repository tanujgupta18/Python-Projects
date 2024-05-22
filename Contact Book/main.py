import tkinter as tk
from tkinter import messagebox
from tkinter import ttk

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def view_contacts(self):
        view_contacts_window = tk.Toplevel()
        view_contacts_window.title("View Contacts")
        view_contacts_window.geometry("800x600")

        contact_tree = ttk.Treeview(view_contacts_window)
        contact_tree['columns'] = ('Name', 'Phone', 'Email', 'Address')
        contact_tree.heading('#0', text='ID')
        contact_tree.heading('Name', text='Name')
        contact_tree.heading('Phone', text='Phone')
        contact_tree.heading('Email', text='Email')
        contact_tree.heading('Address', text='Address')

        for i, contact in enumerate(self.contacts):
            contact_tree.insert('', 'end', text=str(i+1), values=(contact.name, contact.phone, contact.email, contact.address))

        contact_tree.pack(expand=True, fill='both')

        def delete_contact():
            selected_items = contact_tree.selection()
            if selected_items:
                index = int(selected_items[0][1:]) - 1
                contact = self.contacts[index]
                confirm = messagebox.askyesno("Confirm Deletion", f"Are you sure you want to delete {contact.name}?")
                if confirm:
                    self.delete_contact(contact)
                    contact_tree.delete(selected_items)
                    messagebox.showinfo("Success", "Contact deleted successfully.")

        delete_button = ttk.Button(view_contacts_window, text="Delete", command=delete_contact)
        delete_button.pack()

        def edit_contact():
            selected_items = contact_tree.selection()
            if selected_items:
                index = int(selected_items[0][1:]) - 1
                contact = self.contacts[index]
                self.view_edit_contact(contact)

        edit_button = ttk.Button(view_contacts_window, text="Edit", command=edit_contact)
        edit_button.pack()

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query.lower() in contact.phone.lower():
                results.append(contact)
        return results

    def view_edit_contact(self, contact):
        view_edit_contact_window = tk.Toplevel()
        view_edit_contact_window.title("View/Edit Contact")

        tk.Label(view_edit_contact_window, text="Name:").grid(row=0, column=0, padx=5, pady=5)
        name_entry = tk.Entry(view_edit_contact_window)
        name_entry.insert(tk.END, contact.name)
        name_entry.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(view_edit_contact_window, text="Phone:").grid(row=1, column=0, padx=5, pady=5)
        phone_entry = tk.Entry(view_edit_contact_window)
        phone_entry.insert(tk.END, contact.phone)
        phone_entry.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(view_edit_contact_window, text="Email:").grid(row=2, column=0, padx=5, pady=5)
        email_entry = tk.Entry(view_edit_contact_window)
        email_entry.insert(tk.END, contact.email)
        email_entry.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(view_edit_contact_window, text="Address:").grid(row=3, column=0, padx=5, pady=5)
        address_entry = tk.Entry(view_edit_contact_window)
        address_entry.insert(tk.END, contact.address)
        address_entry.grid(row=3, column=1, padx=5, pady=5)

        update_button = ttk.Button(view_edit_contact_window, text="Update", command=lambda: self.update_contact(contact, name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get()))
        update_button.grid(row=4, column=0, pady=10)

    def update_contact(self, contact, name, phone, email, address):
        contact.name = name
        contact.phone = phone
        contact.email = email
        contact.address = address
        messagebox.showinfo("Success", "Contact updated successfully.")

    def delete_contact(self, contact):
        self.contacts.remove(contact)
        messagebox.showinfo("Success", "Contact deleted successfully.")

    def confirm_delete(self, contact, window):
        confirm = messagebox.askyesno("Confirm Deletion", "Are you sure you want to delete this contact?")
        if confirm:
            self.delete_contact(contact)
            window.destroy()

def main():
    contact_book = ContactBook()

    root = tk.Tk()
    root.title("Contact Book")
    root.geometry("800x600")

    style = ttk.Style()
    style.theme_use("clam")

    ttk.Label(root, text="Name:").grid(row=0, column=0, padx=5, pady=5, sticky='e')
    name_entry = tk.Entry(root)
    name_entry.grid(row=0, column=1, padx=5, pady=5)

    ttk.Label(root, text="Phone:").grid(row=1, column=0, padx=5, pady=5, sticky='e')
    phone_entry = tk.Entry(root)
    phone_entry.grid(row=1, column=1, padx=5, pady=5)

    ttk.Label(root, text="Email:").grid(row=2, column=0, padx=5, pady=5, sticky='e')
    email_entry = tk.Entry(root)
    email_entry.grid(row=2, column=1, padx=5, pady=5)

    ttk.Label(root, text="Address:").grid(row=3, column=0, padx=5, pady=5, sticky='e')
    address_entry = tk.Entry(root)
    address_entry.grid(row=3, column=1, padx=5, pady=5)

    add_button = ttk.Button(root, text="Add Contact", command=lambda: add_contact(name_entry.get(), phone_entry.get(), email_entry.get(), address_entry.get(), contact_book))
    add_button.grid(row=4, column=0, columnspan=2, pady=10)

    view_button = ttk.Button(root, text="View Contacts", command=lambda: view_contacts(contact_book))
    view_button.grid(row=5, column=0, columnspan=2, pady=10)

    search_label = ttk.Label(root, text="Search:")
    search_label.grid(row=6, column=0, padx=5, pady=5, sticky='e')
    search_entry = tk.Entry(root)
    search_entry.grid(row=6, column=1, padx=5, pady=5)
    search_button = ttk.Button(root, text="Search", command=lambda: search_contacts(search_entry.get(), contact_book))
    search_button.grid(row=7, column=0, columnspan=2, pady=10)

    root.mainloop()

def add_contact(name, phone, email, address, contact_book):
    contact = Contact(name, phone, email, address)
    contact_book.add_contact(contact)
    messagebox.showinfo("Success", "Contact added successfully.")

def view_contacts(contact_book):
    contact_book.view_contacts()

def search_contacts(query, contact_book):
    results = contact_book.search_contacts(query)
    if results:
        view_edit_contacts(results, contact_book)
    else:
        messagebox.showerror("Error", "No contacts found.")

def view_edit_contacts(contacts, contact_book):
    view_edit_contacts_window = tk.Toplevel()
    view_edit_contacts_window.title("View/Edit Contacts")

    contact_listbox = tk.Listbox(view_edit_contacts_window)
    contact_listbox.pack(fill=tk.BOTH, expand=True)

    for i, contact in enumerate(contacts):
        contact_listbox.insert(tk.END, f"{i+1}. {contact.name} - {contact.phone}")

    view_edit_contact_button = ttk.Button(view_edit_contacts_window, text="View/Edit Contact", command=lambda: contact_book.view_edit_contact(contacts[contact_listbox.curselection()[0]]))
    view_edit_contact_button.pack()

if __name__ == "__main__":
    main()