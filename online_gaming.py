print(" Gaming Login ")

username = input("Username: ")
password = input("Password: ")
banned = input("Account Banned (yes/no): ").lower()

if username == "admin":
    if password == "game123":
        if banned == "no":
            print("Login Successful")
        else:
            print("Account Banned")
    else:
        print("Wrong Password")
else:
    print("Username Not Found")