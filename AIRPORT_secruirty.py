print(" Airport Security ")

passport = input("Passport Available (yes/no): ").lower()
ticket = input("Valid Ticket (yes/no): ").lower()
baggage = float(input("Baggage Weight (kg): "))
dangerous = input("Dangerous Item Found (yes/no): ").lower()

if passport == "yes":
    if ticket == "yes":
        if baggage <= 30:
            if dangerous == "no":
                print("Security Cleared")
            else:
                print("Dangerous Item Detected")
        else:
            print("Baggage Limit Exceeded")
    else:
        print("Invalid Ticket")
else:
    print("❌ Passport Missing")