print("<<<enter your login account info>>>")
user_name=str(input("please enter your username :"))
password=int(input("please enter your current passward :"))

if user_name=="siddique":
    print("correct user name ")
else:
    print("incorrect user name ")

if password==12345678:
    print("correct passward ")

else:   
    print("incorrect passward ")

if user_name == "siddique" and password == 12345678:
    print("Successfully logged in")
else:
    print("Login failed")
