print(" Credit Card Approval ")

salary = int(input("Salary: "))
credit = int(input("Credit Score: "))
loan = input("Existing Loan (yes/no): ").lower()

if salary >= 100000 and credit >= 750 and loan == "no":
    print("Credit Card Approved")
else:
    print("Credit Card Rejected")