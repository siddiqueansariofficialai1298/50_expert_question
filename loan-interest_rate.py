print("===== Loan Interest =====")

credit = int(input("Credit Score: "))
salary = int(input("Monthly Salary: "))

if credit >= 800:
    rate = 5
elif credit >= 700:
    rate = 8
elif credit >= 600:
    rate = 12
else:
    rate = 18

if salary < 50000:
    rate += 2

print("Interest Rate =", rate, "%")