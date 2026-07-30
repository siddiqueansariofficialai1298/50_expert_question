print(" Super Market Billing ")

bill = float(input("Enter Bill Amount: "))
member = input("Membership (yes/no): ").lower()

if bill >= 10000:
    discount = bill * 0.20
elif bill >= 5000:
    discount = bill * 0.10
elif bill >= 2000:
    discount = bill * 0.05
else:
    discount = 0

bill = bill - discount

if member == "yes":
    bill = bill - (bill * 0.05)

print("Discount =", discount)
print("Final Bill =", bill)