print("===== Online Exam =====")

attendance = int(input("Attendance %: "))
fee = input("Fee Paid (yes/no): ").lower()
idcard = input("Student ID Available (yes/no): ").lower()

if attendance >= 75:
    if fee == "yes":
        if idcard == "yes":
            print("Eligible For Exam")
        else:
            print("Student ID Missing")
    else:
        print("Fee Not Paid")
else:
    print("Attendance Short")