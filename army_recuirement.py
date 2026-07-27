print(" Army Recruitment ")

height = float(input("Height (cm): "))
weight = float(input("Weight (kg): "))
medical = input("Medical Passed (yes/no): ").lower()

if height >= 170:
    if weight >= 60:
        if medical == "yes":
            print("Selected")
        else:
            print("Medical Failed")
    else:
        print("Weight Too Low")
else:
    print("Height Too Low")