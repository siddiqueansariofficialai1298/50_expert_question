print(" SIM Verification ")

cnic = input("CNIC Available (yes/no): ").lower()
finger = input("Fingerprint Verified (yes/no): ").lower()

if cnic == "yes":
    if finger == "yes":
        print("SIM Activated")
    else:
        print("Fingerprint Failed")
else:
    print("CNIC Required")