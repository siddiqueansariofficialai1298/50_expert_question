print(" HOSPITAL MANAGEMENT ")

age = int(input("Age: "))
emergency = input("Emergency (yes/no): ").lower()
insurance = input("Insurance (yes/no): ").lower()

if emergency == "yes":
    priority = "HIGH"

elif age >= 60:
    priority = "HIGH"

else:
    priority = "NORMAL"

print("Priority =", priority)

bill = 50000

if insurance == "yes":
    bill -= bill * 0.20

print("Bill =", bill)