# Write a program that takes a number and prints whether it is a palindrome or not.

num = int(input("Enter a number: "))

temp = num
rev = 0

while temp > 0:
    digit = temp % 10
    rev = rev * 10 + digit
    temp //= 10

if num == rev:
    print(f"{num} is a palindrome.")
else:
    print(f"{num} is not a palindrome.")    