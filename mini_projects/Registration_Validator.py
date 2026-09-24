import re

print()

print("----- Registration Validator -----")

print()

while True:

    username = input("Enter username: ")
    email = input("Enter email: ")
    phone = input("Enter phone:+91 ")
    password = input("Enter password: ")

    username_pattern = r"^[A-Za-z][A-Za-z0-9@#$%^&*!]{4,11}$"
    email_pattern = r"^[a-zA-Z0-9._-]+@gmail[.]com$"
    phone_pattern = r"^[6-9]\d{9}$"
    password_pattern = r"^[A-Za-z0-9@#$%^&*!]{8,12}$"

    result_1 = re.search(username_pattern, username)
    result_2 = re.search(email_pattern, email)
    result_3 = re.search(phone_pattern, phone)
    result_4 = re.search(password_pattern, password)

    print()

    print("----- Validation Result -----")

    print()

    if result_1:
        print("Username: Valid")
    else:
        print("Username: Invalid")

    if result_2:
        print("Email: Valid")
    else:
        print("Email: Invalid")

    if result_3:
        print("Phone: Valid")
    else:
        print("Phone: Invalid")

    if result_4:
        print("Password: Valid")
    else:
        print("Password: Invalid")

    print()

    break