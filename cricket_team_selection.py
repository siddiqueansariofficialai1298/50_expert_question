print("===== Cricket Selection =====")

fitness = int(input("Fitness Score: "))
batting = int(input("Batting Average: "))
bowling = int(input("Bowling Average: "))

if fitness >= 80:
    if batting >= 45 or bowling <= 30:
        print("✅ Selected")
    else:
        print("❌ Performance Not Enough")
else:
    print("❌ Fitness Failed")