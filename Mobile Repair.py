print(" Mobile Repair ")

warranty = input("Warranty (yes/no): ").lower()
water = input("Water Damage (yes/no): ").lower()

if warranty == "yes":
    if water == "no":
        print("Free Repair")
    else:
        print("Water Damage Not Covered")
else:
    print("Restaurant TablePaid Service")