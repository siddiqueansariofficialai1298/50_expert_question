print(" Bus Pass ")

student = input("Student (yes/no): ").lower()
card = input("Student Card (yes/no): ").lower()

if student == "yes":
    if card == "yes":
        print("Discount Available")
    else:
        print("Student Card Required")
else:
    print("No Discount")