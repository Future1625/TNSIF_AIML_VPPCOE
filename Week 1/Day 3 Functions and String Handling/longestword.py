# Write a function that takes a sentence and returns the word with the maximum length.

def longest_word(sentence):
    words = sentence.split()
    max_word = max(words, key=len)
    return max_word

text = input("Enter a sentence: ")
print("The longest word is:", longest_word(text))