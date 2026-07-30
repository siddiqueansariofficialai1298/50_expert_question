print(" Swimming Pool ")

age = int(input("Age: "))
membership = input("Membership (yes/no): ").lower()

if membership == "yes":
    if age >= 10:
        print("Entry Allowed")
    else:
        print("Too Young")
else:
    print("Membership Required")