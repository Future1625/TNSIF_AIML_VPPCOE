# Password Strength Validator

password = input("Enter your password: ")

if len(password) < 8:
    print("Weak password")

else:
    upper = False
    lower = False
    digit = False
    special = False

    for ch in password:
        if ch.isupper():
            upper = True
        elif ch.islower():
            lower = True
        elif ch.isdigit():
            digit = True
        else:
            special = True

    if upper and lower and digit and special:
        print("Strong password")
    else:
        print("Moderate passwor")

