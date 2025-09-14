# Write a program that takes a list of integers and prints only the elements that appear exactly once.

nums = input("Enter numbers separated by space: ").split()
nums = [int(x) for x in nums]

unique = [x for x in nums if nums.count(x) == 1]

print("Elements that appear exactly once:", unique)
