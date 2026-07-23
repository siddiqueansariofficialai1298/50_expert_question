print("===== University Fee =====")

fee = 100000

scholarship = input("Scholarship (yes/no): ").lower()
late = input("Late Fee (yes/no): ").lower()

if scholarship == "yes":
    fee -= fee * 0.50

if late == "yes":
    fee += 5000

print("Total Fee =", fee)