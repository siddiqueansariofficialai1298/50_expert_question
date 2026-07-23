print("===== Netflix Subscription =====")

plan = input("Plan (basic/standard/premium): ").lower()
payment = input("Payment Successful (yes/no): ").lower()
student = input("Student (yes/no): ").lower()

if payment == "yes":
    if plan == "basic":
        price = 1000
    elif plan == "standard":
        price = 1800
    elif plan == "premium":
        price = 2500
    else:
        price = 0

    if student == "yes":
        price *= 0.90

    print("Subscription Active")
    print("Payable Amount:", price)
else:
    print("Payment Failed")