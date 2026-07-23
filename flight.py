print("===== Flight Boarding =====")

passport = input("Passport (yes/no): ").lower()
visa = input("Visa (yes/no): ").lower()
ticket = input("Ticket Confirmed (yes/no): ").lower()
weight = float(input("Baggage Weight (kg): "))

if passport == "yes":
    if visa == "yes":
        if ticket == "yes":
            if weight <= 30:
                print("✈ Boarding Allowed")
            else:
                print("❌ Extra Baggage")
        else:
            print("❌ Ticket Not Confirmed")
    else:
        print("❌ Visa Missing")
else:
    print("❌ Passport Missing")