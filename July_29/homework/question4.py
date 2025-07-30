# Multi-Level Loan Eligibility Checker

age = int(input("Enter your age: "))
income = float(input("Enter your monthly income: "))
credit = int(input("Enter your credit score: "))

reasons = []

if age < 21 or age > 60:
    reasons.append("Rejected due to age")

if income < 2500:
    reasons.append("Rejected due to low income")

if credit < 600:
    reasons.append("Rejected due to poor credit score")

if len(reasons) == 0:
    print("Loan Approved")
else:
    for reason in reasons:
        print(reason)