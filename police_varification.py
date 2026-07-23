print("===== POLICE VERIFICATION =====")

cnic = input("CNIC Available (yes/no): ").lower()
criminal = input("Criminal Record (yes/no): ").lower()
address = input("Address Verified (yes/no): ").lower()

if cnic == "yes":

    if criminal == "no":

        if address == "yes":

            print("Verification Successful")

        else:
            print("Address Not Verified")

    else:
        print("Criminal Record Found")

else:
    print("CNIC Missing")