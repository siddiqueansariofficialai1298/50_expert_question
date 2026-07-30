print(" Password Check ")

password = input("Enter Password: ")

if len(password) >= 8:
    if any(ch.isdigit() for ch in password):
        print("Strong Password")
    else:
        print("Add Numbers")
else:
    print("Password Too Short")