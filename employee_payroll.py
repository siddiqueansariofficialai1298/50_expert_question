print(" Employee Payroll ")

salary = float(input("Basic Salary: "))
overtime = int(input("Overtime Hours: "))
loan = float(input("Loan Deduction: "))

total = salary + (overtime * 500)

if total > 100000:
    tax = total * 0.10
else:
    tax = total * 0.05

net_salary = total - tax - loan

print("Net Salary:", net_salary)