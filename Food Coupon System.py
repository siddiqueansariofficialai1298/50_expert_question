print(" Food Coupon ")

bill = float(input("Enter Bill Amount: "))
coupon = input("Coupon Available (yes/no): ").lower()

if coupon == "yes":
    if bill >= 2000:
        bill = bill - 300
        print("Coupon Applied")
    else:
        print("Minimum Bill Not Reached")

print("Final Bill =", bill)