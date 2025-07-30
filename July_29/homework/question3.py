# Traffic Fine Calculator

speed = int(input("Enter your speed (mph): "))
vehicle = input("Enter vehicle type (car/truck/motorcycle): ").lower()

speed_limit = 60
over_speed = speed - speed_limit

fine = 0
suspension = False

if over_speed <= 0:
    print("No fine.")
else:
    if vehicle == "car":
        if over_speed <= 10:
            fine = 50
        elif over_speed <= 20:
            fine = 100
        else:
            fine = 200
            suspension = True

    elif vehicle == "truck":
        if over_speed <= 10:
            fine = 50 * 2
        elif over_speed <= 20:
            fine = 100 * 2
        else:
            fine = 200 * 2
        if over_speed > 15:
            suspension = True

    elif vehicle == "motorcycle":
        if over_speed <= 10:
            fine = 50 // 2
        elif over_speed <= 20:
            fine = 100 // 2
        else:
            fine = 200 // 2
        if over_speed > 25:
            suspension = True

    else:
        print("Invalid vehicle type")
        exit()

    print("Fine: $", fine)
    if suspension:
        print("License suspension warning")