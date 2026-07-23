print("===== Car Insurance =====")

car_age = int(input("Car Age: "))
accidents = int(input("Number of Accidents: "))
premium = 20000

if car_age > 10:
    premium += 5000

if accidents > 2:
    premium += 10000

print("Insurance Premium:", premium)