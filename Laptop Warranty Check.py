print(" Laptop Warranty ")

months = int(input("Warranty Used (Months): "))
damage = input("Physical Damage (yes/no): ").lower()

if months <= 12:
    if damage == "no":
        print("Free Repair")
    else:
        print("Physical Damage Not Covered")
else:
    print("Warranty Expired")