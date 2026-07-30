print(" Courier ")

address = input("Correct Address (yes/no): ").lower()
payment = input("Payment Done (yes/no): ").lower()

if address == "yes":
    if payment == "yes":
        print("Parcel Delivered")
    else:
        print("Payment Pending")
else:
    print("Invalid Address")