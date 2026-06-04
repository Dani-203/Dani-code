phonebook = {}
def add_connect() :
    name = input("Enter name: ").strip()
    if name in phonebook:
        print("Contact already exists!")
    else:
        number = input("Enter Phone Number: ").strip()
        phonebook[name] = number
        print(f"Contact {name} added successfully!")

def search_contact():
    name = input("Enter Name to Search: ").strip()
    if name in phonebook:
        print(f"{name}'s number: {phonebook[name]}")
    else:
        print("Contact not found!")

def display_contacts():
    if not phonebook:
        print("Phonebook is empty.")
    else:
        print("/n--- Phonebook ---")
        for name, number in phonebook.items():
           print(f"{name}; {number}")
