# 1.	Write a program to take 5 numbers from the user and store them in a tuple, then print the maximum and minimum.

nums = []
for i in range(5):
    num = int(input(f"Enter number {i+1}: "))
    nums.append(num)

numbers = tuple(nums)

print("Tuple:", numbers)
print("Maximum:", max(numbers))
print("Minimum:", min(numbers))