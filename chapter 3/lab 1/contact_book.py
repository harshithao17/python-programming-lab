contacts = []

n = int(input("Enter number of contacts: "))

for i in range(n):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")

    contact = {
        "Name": name,
        "Phone": phone
    }

    contacts.append(contact)

print("\nCONTACT BOOK")

for contact in contacts:
    print("Name:", contact["Name"])
    print("Phone:", contact["Phone"])
    print("----------------")