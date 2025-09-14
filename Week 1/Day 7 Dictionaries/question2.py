# Write a program to map roll numbers to names using two lists and form a dictionary.

roll_numbers = input("Enter roll numbers separated by space: ").split()
names = input("Enter names separated by space: ").split()

student_dict = {}

for i in range(len(roll_numbers)):
    student_dict[roll_numbers[i]] = names[i]

print("Roll number to Name mapping:", student_dict)