# Contact Management System in Python

contacts = []  # list to store all contacts as dictionaries


def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")

    contact = {
        "name": name,
        "phone": phone,
        "email": email,
        "address": address
    }
    contacts.append(contact)
    print("✅ Contact added successfully!")


def view_contacts():
    if not contacts:
        print("No contacts found.")
        return
    print("\n📒 Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")


def search_contact():
    search = input("Enter Name or Phone to search: ")
    found = [c for c in contacts if c["name"] == search or c["phone"] == search]

    if found:
        for c in found:
            print(f"\n🔎 Found Contact:")
            print(f"Name: {c['name']}")
            print(f"Phone: {c['phone']}")
            print(f"Email: {c['email']}")
            print(f"Address: {c['address']}")
    else:
        print("❌ Contact not found.")


def update_contact():
    search = input("Enter the Name of the contact to update: ")
    for c in contacts:
        if c["name"] == search:
            print("Leave blank if you don't want to update a field.")
            new_phone = input("New Phone: ") or c["phone"]
            new_email = input("New Email: ") or c["email"]
            new_address = input("New Address: ") or c["address"]

            c["phone"], c["email"], c["address"] = new_phone, new_email, new_address
            print("✅ Contact updated successfully!")
            return
    print("❌ Contact not found.")


def delete_contact():
    search = input("Enter the Name of the contact to delete: ")
    for c in contacts:
        if c["name"] == search:
            contacts.remove(c)
            print("🗑️ Contact deleted successfully!")
            return
    print("❌ Contact not found.")


# Main program loop
while True:
    print("\n===== Contact Management System =====")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

    choice = input("Choose an option (1-6): ")

    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        print("👋 Exiting... Goodbye!")
        break
    else:
        print("❌ Invalid choice. Please try again.")
