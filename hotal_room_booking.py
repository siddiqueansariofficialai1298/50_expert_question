print("===== Hotel Booking =====")

days = int(input("Days: "))
room = input("Room (standard/deluxe/suite): ").lower()

if room == "standard":
    rate = 3000
elif room == "deluxe":
    rate = 5000
elif room == "suite":
    rate = 8000
else:
    rate = 0

bill = days * rate

if days >= 7:
    bill *= 0.90

print("Total Bill =", bill)