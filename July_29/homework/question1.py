#grade evaluation with attendance

score = int(input("Enter your score: "))
attendance = int(input("Enter your attendance percentage (0-100): "))

if score >= 50:
    if attendance >= 75:
        print("pass")
    else:
        print("Fail due to low attendance")
else:
    if attendance >= 75:
        print("Fail due to score")
    else:
        print("Fail due to score and attendance")