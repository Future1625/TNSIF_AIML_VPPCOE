# Write a program to reverse the contents of a tuple without using reversed().

nums = tuple(map(int, input("Enter numbers separated by space: ").split()))

rev_tuple = nums[::-1]

print("Original tuple:", nums)
print("Reversed tuple:", rev_tuple)