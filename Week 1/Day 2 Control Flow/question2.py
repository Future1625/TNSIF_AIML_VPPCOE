# Write a program that prints all numbers from 1 to 100 that are divisible by 7 but not a multiple of 5.

for num in range(1, 101):
    if num % 7 == 0 and num % 5 != 0:
        print(num)