print(" Cinema Ticket ")

age = int(input("Enter Age: "))
ticket = input("Ticket Booked (yes/no): ").lower()
id_card = input("ID Card Available (yes/no): ").lower()

if ticket == "yes":
    if age >= 18:
        if id_card == "yes":
            print("Entry Allowed")
        else:
            print("ID Card Required")
    else:
        print("Under Age")
else:
    print("Ticket Not Booked")