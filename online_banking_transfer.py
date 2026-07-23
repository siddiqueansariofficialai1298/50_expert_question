print("===== Online Banking Transfer =====")

balance = 100000
pin = 1234

user_pin = int(input("Enter PIN: "))
receiver = input("Receiver Verified (yes/no): ").lower()
amount = float(input("Transfer Amount: "))

if user_pin == pin:
    if receiver == "yes":
        if amount <= balance:
            if amount <= 50000:
                balance -= amount
                print("✅ Transfer Successful")
                print("Remaining Balance:", balance)
            else:
                print("❌ Daily Transfer Limit Exceeded")
        else:
            print("❌ Insufficient Balance")
    else:
        print("❌ Receiver Not Verified")
else:
    print("❌ Incorrect PIN")