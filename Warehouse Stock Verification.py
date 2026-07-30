print(" Warehouse Stock ")

stock = int(input("Current Stock: "))
order = int(input("Order Quantity: "))

if stock >= order:
    stock = stock - order
    print("Order Confirmed")
    print("Remaining Stock =", stock)
else:
    print("Not Enough Stock")