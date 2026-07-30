print(" College Hostel ")

distance = int(input("Distance From College (KM): "))
fee = input("Fee Paid (yes/no): ").lower()

if distance >= 50:
    if fee == "yes":
        print("Hostel Allotted")
    else:
        print("Fee Pending")
else:
    print("Food Coupon SystemHostel Not Required")