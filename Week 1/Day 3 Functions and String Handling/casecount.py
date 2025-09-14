#	Write a function to count the number of uppercase and lowercase characters in a string.

def count_case(s):
    upper = 0
    lower = 0
    for ch in s:
        if ch.isupper():
            upper += 1
        elif ch.islower():
            lower += 1
    return upper, lower

text = input("Enter a string: ")
upper_count, lower_count = count_case(text)

print("Uppercase letters:", upper_count)
print("Lowercase letters:", lower_count)
