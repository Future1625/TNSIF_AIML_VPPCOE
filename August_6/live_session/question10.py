# Combined(List + Dict) - given a list of student names and their marks in a dictionary, write a function to return the names of students with the highest marks

def top_students(students, marks):
    max_marks = max(marks.values())
    return [student for student in students if marks[student] == max_marks]

students = ['Alice', 'Bob', 'Charlie']
marks = {'Alice': 90, 'Bob': 85, 'Charlie': 95}
result = top_students(students, marks)
print("Students with the highest marks:", result)    