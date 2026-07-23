print("===== ATM MACHINE =====")

balance = 100000
pin = 1234

user_pin = int(input("Enter PIN: "))

if user_pin == pin:

    print("""
1. Balance Inquiry
2. Cash Withdrawal
3. Cash Deposit
4. Exit
""")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        print("Current Balance =", balance)

    elif choice == 2:

        amount = float(input("Withdrawal Amount: "))

        if amount <= balance:
            if amount % 500 == 0:
                balance -= amount
                print("Withdrawal Successful")
                print("Remaining Balance =", balance)
            else:
                print("Amount should be multiple of 500")
        else:
            print("Insufficient Balance")

    elif choice == 3:

        deposit = float(input("Deposit Amount: "))
        balance += deposit

        print("Deposit Successful")
        print("Current Balance =", balance)

    elif choice == 4:
        print("Thank You")

    else:
        print("Invalid Choice")

else:
    print("Incorrect PIN")