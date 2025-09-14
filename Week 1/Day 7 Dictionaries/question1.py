# Write a program that takes a sentence and creates a dictionary with word counts

sentence = input("Enter a sentence: ").lower()

words = sentence.split()
word_count = {}

for word in words:
    word_count[word] = word_count.get(word, 0) + 1

print("Word counts:", word_count)