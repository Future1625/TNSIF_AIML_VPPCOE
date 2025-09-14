# Write a program to take two lists from the user and print the common elements using sets.

list1 = list(map(int, input("Enter elements of first list separated by space: ").split()))
list2 = list(map(int, input("Enter elements of second list separated by space: ").split()))

common = set(list1) & set(list2)

print("Common elements:", common)