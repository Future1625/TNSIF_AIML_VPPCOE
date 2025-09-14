# Write a program to remove all elements at odd indices from a list.

nums = input("Enter numbers separated by space: ").split()
nums = [int(x) for x in nums]

result = [nums[i] for i in range(len(nums)) if i % 2 == 0]

print("List after removing odd indices:", result)