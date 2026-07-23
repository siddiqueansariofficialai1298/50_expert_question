print("===== ATM =====")

balance = 50000

choice = input("Deposit or Withdraw: ").lower()
amount = int(input("Amount: "))

if choice == "deposit":
    balance += amount
    print("Deposit Successful")
    print("Balance =", balance)

elif choice == "withdraw":

    if amount <= balance:
        balance -= amount
        print("Withdrawal Successful")
        print("Balance =", balance)
    else:
        print("Insufficient Balance")

else:
    print("Invalid Choice")