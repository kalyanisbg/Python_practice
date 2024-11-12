# Create a Simple Contact Book

# Goal: Write a program that allows users to add, view, and search for contacts in a contact book.

##  Instructions 
# Define a Contact List: Create an empty list to hold the contacts.
contact_list = {}
# Define Functions: Write functions to add a contact, view all contacts, and search for a contact by name.
def add_contact(name, contact_num):
    contact_list[name] = contact_num
    return contact_list

def view_all_contacts(name):
    print(contact_list)

def search_contacts(name):
    if name in contact_list:
        print(f"Contact number: {contact_list[name]}")
    else:
        print(f"{name} not in contacts")
        
# User Interaction: Allow the user to choose an action and execute the corresponding function.