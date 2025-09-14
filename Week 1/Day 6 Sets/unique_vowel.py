# Write a program to find all unique vowels present in a given string using set.

text = input("Enter a string: ").lower()

vowels = set("aeiou")
found = set(text) & vowels 

print("Unique vowels present:", found) 