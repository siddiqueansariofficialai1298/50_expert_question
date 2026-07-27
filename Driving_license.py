print(" Driving License ")

age = int(input("Age: "))
eye = input("Eye Test (pass/fail): ").lower()
written = input("Written Test (pass/fail): ").lower()
road = input("Road Test (pass/fail): ").lower()

if age >= 18:
    if eye == "pass":
        if written == "pass":
            if road == "pass":
                print(" License Approved")
            else:
                print(" Road Test Failed")
        else:
            print(" Written Test Failed")
    else:
        print(" Eye Test Failed")
else:
    print(" Under Age")