print(" Train Reservation ")

seats = int(input("Available Seats: "))
age = int(input("Age: "))
gender = input("Gender: ").lower()

if seats > 0:
    if age >= 60:
        print("Seat Reserved (Senior Citizen)")
    elif gender == "female":
        print("Seat Reserved (Ladies Quota)")
    else:
        print("Seat Reserved (General)")
else:
    print("No Seats Available")