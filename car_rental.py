print("===== Car Rental =====")

age = int(input("Age: "))
license = input("Driving License (yes/no): ").lower()
deposit = int(input("Security Deposit: "))

if age >= 21:
    if license == "yes":
        if deposit >= 10000:
            print("Car Rental Approved")
        else:
            print("Deposit Too Low")
    else:
        print("Driving License Required")
else:
    print("Age Requirement Not Met")