print("===== School Result =====")

english = int(input("English: "))
math = int(input("Math: "))
science = int(input("Science: "))
computer = int(input("Computer: "))
urdu = int(input("Urdu: "))

total = english + math + science + computer + urdu
percentage = total / 5

if english < 40 or math < 40 or science < 40 or computer < 40 or urdu < 40:
    print("❌ FAIL")
else:
    print("Percentage =", percentage)

    if percentage >= 90:
        print("Grade A+")
    elif percentage >= 80:
        print("Grade A")
    elif percentage >= 70:
        print("Grade B")
    elif percentage >= 60:
        print("Grade C")
    else:
        print("Grade D")