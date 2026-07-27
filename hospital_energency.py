print(" Hospital Priority  ")

age = int(input("Age: "))
emergency = input("Emergency (yes/no): ").lower()
fever = input("Fever (yes/no): ").lower()

if emergency == "yes":
    print("Priority Level: HIGH")
elif age >= 60:
    print("Priority Level: HIGH")
elif fever == "yes":
    print("Priority Level: HIGH")
else:
    print("Priority Level: NORMAL")