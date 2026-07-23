print("===== Income Tax Calculator =====")

income = int(input("Annual Income: "))

if income <= 600000:
    tax = 0
elif income <= 1200000:
    tax = income * 0.05
elif income <= 2400000:
    tax = income * 0.10
elif income <= 5000000:
    tax = income * 0.15
else:
    tax = income * 0.20

print("Tax =", tax)