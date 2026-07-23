print("===== Salary Calculator =====")

basic = float(input("Basic Salary: "))
overtime = int(input("Overtime Hours: "))
late = int(input("Late Days: "))

salary = basic + (overtime * 500)

if late > 5:
    salary -= 2000

print("Final Salary =", salary)