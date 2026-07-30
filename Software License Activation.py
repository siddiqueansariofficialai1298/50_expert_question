print(" Software Activation ")

key = input("Enter License Key: ")
internet = input("Internet Available (yes/no): ").lower()

if len(key) == 16:
    if internet == "yes":
        print("Software Activated")
    else:
        print("Internet Required")
else:
    print("Invalid License Key")