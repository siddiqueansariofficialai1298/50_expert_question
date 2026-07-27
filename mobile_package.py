print(" Mobile Package ")

recharge = int(input("Recharge Amount: "))

if recharge >= 5000:
    print("Unlimited Calls + 100GB Internet")
elif recharge >= 3000:
    print("Unlimited Calls + 50GB Internet")
elif recharge >= 1000:
    print("500 Minutes + 20GB Internet")
else:
    print("Basic Package")