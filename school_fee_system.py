print("===== School Fee =====")

fee = 50000

scholarship = input("Scholarship (yes/no): ").lower()
siblings = int(input("Number of Siblings: "))
late = input("Late Fee (yes/no): ").lower()

if scholarship == "yes":
    fee -= 10000

if siblings >= 2:
    fee -= 5000

if late == "yes":
    fee += 3000

print("Final Fee:", fee)