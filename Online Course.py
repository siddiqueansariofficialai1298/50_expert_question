print(" Online Course ")

payment = input("Payment Done (yes/no): ").lower()
email = input("Email Verified (yes/no): ").lower()

if payment == "yes":
    if email == "yes":
        print("Course Unlocked")
    else:
        print("Verify Email")
else:
    print("Payment Pending")