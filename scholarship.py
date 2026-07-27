print(" Scholarship Eligibility ")

marks = float(input("Enter Marks (%): "))
attendance = float(input("Enter Attendance (%): "))
income = int(input("Enter Family Income: "))

if marks >= 90:
    if attendance >= 85:
        if income <= 50000:
            print("Scholarship Approved")
        else:
            print("Income Too High")
    else:
        print("Attendance Too Low")
else:
    print("Marks Too Low")