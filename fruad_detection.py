print("===== Fraud Detection =====")

amount = int(input("Transaction Amount: "))
country = input("Foreign Country? (yes/no): ").lower()
otp = input("OTP Verified? (yes/no): ").lower()

if amount > 100000:
    if country == "yes":
        if otp == "no":
            print("🚨 Fraud Alert")
        else:
            print("Transaction Approved")
    else:
        print("Transaction Approved")
else:
    print("Transaction Approved")