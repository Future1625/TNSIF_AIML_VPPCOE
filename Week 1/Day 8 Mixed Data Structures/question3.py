# 3.Write a program that takes a list with duplicate elements and returns a dictionary with elements as keys and their frequency as values.

nums = list(map(int, input("Enter numbers separated by space: ").split()))

freq_dict = {}
for num in nums:
    freq_dict[num] = freq_dict.get(num, 0) + 1

print("Frequency dictionary:", freq_dict)