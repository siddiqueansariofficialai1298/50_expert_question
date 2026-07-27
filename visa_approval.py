print(" Visa Approval ")

passport = input("Passport (yes/no): ").lower()
bank = int(input("Bank Balance: "))
criminal = input("Criminal Record (yes/no): ").lower()

if passport == "yes":
    if bank >= 1000000:
        if criminal == "no":
            print("Visa Approved")
        else:
            print("Visa Rejected (Criminal Record)")
    else:
        print("Insufficient Bank Balance")
else:
    print("Passport Missing")