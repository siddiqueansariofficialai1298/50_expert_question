print(" Passport Renewal ")

expired = input("Passport Expired (yes/no): ").lower()
fee = input("Fee Paid (yes/no): ").lower()

if expired == "yes":
    if fee == "yes":
        print("Passport Renewed")
    else:
        print("Fee Pending")
else:
    print("Passport Still Valid")