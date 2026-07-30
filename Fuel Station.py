print(" Fuel Station ")

fuel = float(input("Fuel Liters: "))
member = input("Member (yes/no): ").lower()

bill = fuel * 280

if member == "yes":
    bill -= bill * 0.05

print("Total Bill =", bill)