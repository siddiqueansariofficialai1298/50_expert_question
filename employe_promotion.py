print(" Employee Promotion ")

experience = int(input("Experience (Years): "))
performance = int(input("Performance Score: "))
attendance = int(input("Attendance (%): "))

if experience >= 5:
    if performance >= 90:
        if attendance >= 95:
            print("Promotion Approved")
        else:
            print("Attendance Too Low")
    else:
        print("Performance Too Low")
else:
    print("Experience Too Low")