print(" Library ")

member = input("Member (yes/no): ").lower()
fine = int(input("Pending Fine: "))

if member == "yes":
    if fine == 0:
        print("Book Issued")
    else:
        print("Clear Fine First")
else:
    print("Membership Required")