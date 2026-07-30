print(" Driving School Admission ")

age = int(input("Enter Age: "))
cnic = input("CNIC Available (yes/no): ").lower()
medical = input("Medical Fit (yes/no): ").lower()

if age >= 18:
    if cnic == "yes":
        if medical == "yes":
            print("Admission Approved")
        else:
            print("Medical Test Failed")
    else:
        print("CNIC Required")
else:
    print("Under Age")