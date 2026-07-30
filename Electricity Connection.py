print(" Electricity Connection ")

cnic = input("CNIC (yes/no): ").lower()
bill = input("Previous Bills Cleared (yes/no): ").lower()

if cnic == "yes":
    if bill == "yes":
        print("New Connection Approved")
    else:
        print("Clear Previous Bills")
else:
    print("CNIC Missing")