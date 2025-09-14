# Write a program to find the difference between the maximum and minimum elements in a list.


nums = input("Enter numbers separated by space: ")
nums = nums.split()
numbers = [int(x) for x in nums]

print("Difference is:", max(numbers) - min(numbers))