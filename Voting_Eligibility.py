print("===== Voting System =====")

age = int(input("Age: "))
cnic = input("CNIC Available (yes/no): ").lower()
voted = input("Already Voted? (yes/no): ").lower()

if age >= 18:
    if cnic == "yes":
        if voted == "no":
            print("You Can Vote")
        else:
            print("Already Voted")
    else:
        print("CNIC Required")
else:
    print("Under Age")