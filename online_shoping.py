print("===== Online Shopping =====")

bill = float(input("Enter Purchase Amount: "))
premium = input("Premium Member (yes/no): ").lower()
coupon = input("Coupon Available (yes/no): ").lower()

if premium == "yes":
    bill = bill - (bill * 0.10)

if coupon == "yes":
    bill = bill - (bill * 0.05)

if bill > 3000:
    delivery = 0
else:
    delivery = 250

total = bill + delivery

print("Final Bill:", bill)
print("Delivery Charges:", delivery)
print("Payable Amount:", total)