print(" Mobile Exchange ")

working = input("Phone Working (yes/no): ").lower()
age = int(input("Phone Age (Years): "))

if working == "yes":
    if age <= 2:
        print("Exchange Value = 60000")
    elif age <= 4:
        print("Exchange Value = 40000")
    else:
        print("Exchange Value = 15000")
else:
    print("Phone Not Eligible")