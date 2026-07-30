print(" Restaurant ")

table = input("Table Available (yes/no): ").lower()
booking = input("Booking (yes/no): ").lower()

if table == "yes":
    print("Seat Available")
elif booking == "yes":
    print("Please Wait")
else:
    print("No Table")