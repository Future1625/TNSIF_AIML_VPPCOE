# write a function to check whether a given string is a pangram (contains all letters of the alphabet).

def is_pangram(sentence):
    sentence = sentence.lower()
    for ch in "abcdefghijklmnopqrstuvwxyz":
        if ch not in sentence:
            return False
    return True

text = input("Enter a sentence: ")
if is_pangram(text):
    print("It is a pangram")
else:
    print("It is not a pangram")
