print(" Hotel Booking ")

days = int(input("Days: "))
room = input("Room (standard/deluxe): ").lower()

if room == "standard":
    bill = days * 3000
elif room == "deluxe":
    bill = days * 6000
else:
    bill = 0

coupon = input("Coupon Available (yes/no): ").lower()

if coupon == "yes":
    bill *= 0.9

print("Total Bill =", bill)