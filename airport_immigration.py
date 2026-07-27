print(" IMMIGRATION ")

passport = input("Passport (yes/no): ").lower()
visa = input("Visa (yes/no): ").lower()
ticket = input("Ticket (yes/no): ").lower()

if passport == "yes":

    if visa == "yes":

        if ticket == "yes":

            print("Immigration Cleared")

        else:
            print("Ticket Missing")

    else:
        print("Visa Missing")

else:
    print("Passport Missing")