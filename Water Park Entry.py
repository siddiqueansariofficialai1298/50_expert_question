print(" Water Park ")

height = float(input("Height (cm): "))
ticket = input("Ticket (yes/no): ").lower()

if ticket == "yes":
    if height >= 120:
        print("Ride Allowed")
    else:
        print("Height Too Short")
else:
    print("Buy Ticket First")