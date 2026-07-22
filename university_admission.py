eng=float(input("Enter your English marks:/n"))
urdu=float(input("Enter your urdu marks:/n"))
chemistry=float(input("Enter your chemistry marks:/n"))
math=float(input("Enter your math marks:/n"))
physics=float(input("Enter your physics marks:/n"))
bio=float(input("Enter your bio marks:/n"))
islamiat=float(input("Enter your islamiat marks:/n"))

obtained_marks=eng+urdu+chemistry+math+physics+bio+islamiat
print("obtained marks:", obtained_marks)
percentage=obtained_marks/700*100
print("percentage:",percentage)

if percentage<=100 and percentage>=90:
    print("interview successfull")
else:
    print("sorry! you are rejected. beacuse your percentage is less than 90")