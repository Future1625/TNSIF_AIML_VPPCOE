def conditional(a, b):
    if (a > b):
        for i in range(1, 6):
            print(f"{a} is greater than {b}")
    else:
        for i in range(1, 6):
            print(f"{b} is greater than or equal to {a}")

conditional(10,5)
