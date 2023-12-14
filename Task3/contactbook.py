contacts={}


def add_contact(name,phone,email,address):
    contacts[name]={'phone': phone, 'email': email,'address': address}
    print(f"\nContact {name} added successfully")

def search_contact(name):
    if name in contacts:
        print(f"\n Name:{name}")
        print(f"Phone:{contacts[name]['phone']}")
        print(f"Email:{contacts[name]['email']}")
        print(f"Address:{contacts[name]['address']}")
    else:
        print(f"Contact {name} not found")
def display_contacts():
    if contacts:
        print("\nContact list:")
        for name,info in contacts.items():
            print(f"Name:{name}")
            print(f"Phone:{info['phone']}")
            print(f"Email:{info['email']}")
            print(f"Address:{info['address']}")
            print()
    else:
        print("The contact book is empty")

def delete_contact(name):
    if name in contacts:
        del contacts [name]
        print(f"\n Contact {name} deleted successfully")
    else:
        print(f"Contact {name} not found")
def update_contact(name):
    if name in contacts:
        new_phone=input(f"enter new phone number for {name}:")
        new_email=input(f"enter new email for {name}:")
        new_address=input(f"enter new address for {name}:")
        contacts[name]['phone']=new_phone
        contacts[name]['email']=new_email
        contacts[name]['address']=new_address
        print(f"\ncontact {name} updated succesfully")
    else:
        print(f"contact{name} not found")    
while True:
    print("\n Contact book:")
    print("1.Add")
    print("2.Search")
    print("3.Display")
    print("4.Delete")
    print("5.Update")
    print("6.Quit")
    
    choice=input("Enter your choice:")

    if choice=='1':
        name=input("Enter name:")
        phone=input("Enter phone number:")
        email=input("Enter email:")
        address=input("Enter address:")
        add_contact(name,phone,email,address)
    elif choice=="2":
        name=input("Enter name to search:")
        search_contact(name)
    elif choice=="3":
        display_contacts()
    elif choice=="4":
        name=input("Enter name to delete:")
        delete_contact(name)
    elif choice=="5":
        name=input("Enter name to update:")
        update_contact(name)
    elif choice=="6":
        print("exiting contact book")
        break
    else:
        print("Invalid choice. Please choose a valid option")
