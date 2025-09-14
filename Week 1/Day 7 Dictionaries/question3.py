# Write a program that takes a dictionary of students and their marks, and prints the name(s) of the student(s) with the highest marks.

data = input("Enter student names and marks (name mark pairs): ").split()

students = {}
for i in range(0, len(data), 2):
    name = data[i]
    marks = int(data[i+1])
    students[name] = marks

max_marks = max(students.values())

top_students = [name for name, marks in students.items() if marks == max_marks]

print("Student(s) with highest marks:", top_students)