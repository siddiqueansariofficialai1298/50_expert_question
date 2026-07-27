print(" Insurance Premium ")

age = int(input("Age: "))
smoker = input("Smoker (yes/no): ").lower()
disease = input("Heart Disease (yes/no): ").lower()

if age < 30:
    premium = 1000
elif age < 50:
    premium = 2000
else:
    premium = 4000

if smoker == "yes":
    premium += 1500

if disease == "yes":
    premium += 2000

print("Total Premium =", premium)