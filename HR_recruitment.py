print(" HR RECRUITMENT ")

degree = input("Degree (yes/no): ").lower()
experience = int(input("Experience: "))
english = input("English Test Passed (yes/no): ").lower()

if degree == "yes":

    if experience >= 2:

        if english == "yes":

            print("Selected")

        else:
            print("English Test Failed")

    else:
        print("Experience Required")

else:
    print("Degree Required")