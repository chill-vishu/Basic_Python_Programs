#   1. Personal Information
#   Write a program that displays the following information:
#   • Your name
#   • Your address, with city, state, and ZIP
#   • Your telephone numbers
#   • Your college major


# Code :-

def personal_info():
    name = input("Enter your name: ")
    address = input("Enter your address (include city, state, ZIP): ")
    telephone = input("Enter your telephone number: ")
    major = input("Enter your college major: ")
    
    print("\nPersonal Information:")
    print(f"Name: {name}")
    print(f"Address: {address}")
    print(f"Telephone Number: {telephone}")
    print(f"College Major: {major}")

# Calling Function To Execute
personal_info()
