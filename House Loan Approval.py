print(" House Loan ")

salary = int(input("Monthly Salary: "))
credit = int(input("Credit Score: "))
property_price = int(input("Property Price: "))

if salary >= 100000:
    if credit >= 750:
        if property_price >= 5000000:
            print("Loan Approved")
        else:
            print("Property Price Too Low")
    else:
        print("Credit Score Too Low")
else:
    print("Salary Too Low")