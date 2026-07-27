print(" UNIVERSITY ADMISSION ")

inter = float(input("Intermediate %: "))
entry = float(input("Entry Test %: "))
interview = input("Interview (pass/fail): ").lower()

if inter >= 70:

    if entry >= 75:

        if interview == "pass":

            print("Admission Confirmed")

        else:
            print("Interview Failed")

    else:
        print("Entry Test Failed")

else:
    print("Intermediate Marks Low")