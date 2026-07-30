print(" Pet Adoption ")

age = int(input("Age: "))
income = int(input("Monthly Income: "))
house = input("Own House (yes/no): ").lower()

if age >= 21:
    if income >= 50000:
        if house == "yes":
            print("Adoption Approved")
        else:
            print("Own House Required")
    else:
        print("Income Too Low")
else:
    print("Age Must Be 21+")