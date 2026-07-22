amount = float(input("Enter Shopping Amount: "))
member = input("Are you a member? (yes/no): ").lower()

discount = 0

if amount >= 10000:
    discount = 20

elif amount >= 5000:
    discount = 10

elif amount >= 2000:
    discount = 5


if member == "yes":
    discount += 5


final_price = amount - (amount * discount / 100)

print("Discount:", discount, "%")
print("Final Price:", final_price)
