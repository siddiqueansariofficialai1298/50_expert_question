print(" Hostel Allotment ")

merit = float(input("Merit Percentage: "))
distance = int(input("Distance from University (KM): "))
fee = input("Fee Paid (yes/no): ").lower()

if merit >= 75:
    if distance >= 50:
        if fee == "yes":
            print("Hostel Allotted")
        else:
            print("Hostel Fee Pending")
    else:
        print("Distance Too Short")
else:
    print("Merit Too Low")