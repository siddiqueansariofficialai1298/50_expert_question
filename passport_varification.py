print("===== Passport Verification =====")

cnic = input("Valid CNIC (yes/no): ").lower()
police = input("Police Verification (yes/no): ").lower()
fee = input("Fee Paid (yes/no): ").lower()

if cnic == "yes":
    if police == "yes":
        if fee == "yes":
            print("Passport Approved")
        else:
            print("Fee Pending")
    else:
        print("Police Verification Failed")
else:
    print("Invalid CNIC")