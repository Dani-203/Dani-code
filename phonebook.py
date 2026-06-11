phonebook = {}
def add_contact() :
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

def update_contact():
    name = input("Enter Name to Update: ").strip()
    if name in phonebook:
        new_number = input("Enter New Number: ").strip()
        phonebook[name] = new_number
        print(f"Contact {name} updated successfully!")
    else:
        print("Contact not found!")

def delete_contact():
    name = input("Enter Name to Delete: ").strip()
    if name in phonebook:
        del phonebook[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print("Contact not found!")
def main():
    while True:
        print("\n------------------- PHONEBOOK MENU ------------------------")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Display Concacts")
        print("4. Update Contact")
        print("5. Delete Contract")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")
        if choice == '1':
            add_contact()
        elif choice == '2':
            search_contact()
        elif choice == '3':
            display_contacts()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting Phonebook. Goodbye!")
            break
        else:
            print("Invalid choice! Please try again")

# Run the phonebook program
main()
