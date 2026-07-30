print(" Fixed Deposit ")

age = int(input("Enter Age: "))
deposit = float(input("Deposit Amount: "))

if age >= 18:
    if deposit >= 50000:
        print("Fixed Deposit Approved")
    else:
        print("Deposit Too Low")
else:
    print("Age Must Be 18+")