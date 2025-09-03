# Dictionary = write a python program to count the frequency of each character in a string using a dictionary

def char_frequency(string):
    frequency = {}
    for char in string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    return frequency

string = "hello world"
result = char_frequency(string)
print("Character frequency:", result)