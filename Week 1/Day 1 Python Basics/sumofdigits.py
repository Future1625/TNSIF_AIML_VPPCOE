# Write a program that takes a 4-digit number from the user and prints the sum of its digits.

num = int(input("Enter a 4-digit number: "))

digit_sum = 0

while num > 0:
    digit_sum += num % 10
    num //= 10

print("The sum of the digits is:", digit_sum)