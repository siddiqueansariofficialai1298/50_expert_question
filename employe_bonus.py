print("===== Employee Bonus =====")

salary = float(input("Salary: "))
performance = int(input("Performance (1-100): "))
experience = int(input("Experience (Years): "))

bonus = 0

if performance >= 90:
    bonus += salary * 0.20
elif performance >= 80:
    bonus += salary * 0.10

if experience >= 10:
    bonus += salary * 0.05

print("Bonus =", bonus)