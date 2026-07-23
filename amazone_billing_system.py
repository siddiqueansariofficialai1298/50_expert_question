print("===== AMAZON BILLING =====")

bill = float(input("Shopping Amount: "))

prime = input("Prime Member (yes/no): ").lower()
coupon = input("Coupon (yes/no): ").lower()

if prime == "yes":
    bill -= bill * 0.10

if coupon == "yes":
    bill -= bill * 0.05

if bill > 5000:
    shipping = 0
else:
    shipping = 300

gst = bill * 0.18

print("Shipping =", shipping)
print("GST =", gst)
print("Total =", bill + gst + shipping)