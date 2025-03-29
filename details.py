def get_person_details():
    """
    function to read a persons details from the keyboard.
    """
    name =input("Enter your name:")
    address =input("Enter your adress:")
    email =input("Enter your email:")
    phone =input("Enter your phone number:")
    return name,address,email,phone
def print_person_details(name,adress,email,phone):
    """
     function to read a persons details.
    """
    print("\n---personal details---")
    print(f"Name:{name}")
    print(f"Address:{address}")
    print(f"Email:{email}")
    print(f"Phone number:{phone}")
name,address,email,phone=get_person_details()
print_person_details(name,address,email,phone)

