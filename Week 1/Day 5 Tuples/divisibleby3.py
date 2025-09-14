# Given a tuple of integers, write a program to count how many elements are divisible by 3.

nums = tuple(map(int, input("Enter numbers separated by space: ").split()))

count = 0
for n in nums:
    if n % 3 == 0:
        count += 1

print("Tuple:", nums)
print("Count of elements divisible by 3:", count)