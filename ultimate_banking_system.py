print(" MINI BANKING SYSTEM ")

balance = 100000
pin = 1234

user_pin = int(input("Enter PIN: "))

if user_pin == pin:

    print("""
1. Balance
2. Deposit
3. Withdraw
4. Transfer
""")

    choice = int(input("Choice: "))

    if choice == 1:

        print("Balance =", balance)

    elif choice == 2:

        amount = float(input("Deposit: "))
        balance += amount

        print("Updated Balance =", balance)

    elif choice == 3:

        amount = float(input("Withdraw: "))

        if amount <= balance:

            balance -= amount

            print("Remaining Balance =", balance)

        else:

            print("Insufficient Balance")

    elif choice == 4:

        receiver = input("Receiver Verified (yes/no): ").lower()
        amount = float(input("Transfer Amount: "))

        if receiver == "yes":

            if amount <= balance:

                balance -= amount

                print("Transfer Successful")

                print("Remaining Balance =", balance)

            else:

                print("Insufficient Balance")

        else:

            print("Receiver Not Verified")

    else:

        print("Invalid Choice")

else:

    print("Incorrect PIN")