# Write a program to accept marks of 6 students and display them in a sorted manner
marks = []
n = int(input("Enter the number of students:"))

# Using for loop insert the elements inside the array
for mark in range (n):
    element = int(input(f"Enter the mark of student{mark+1}:"))
    marks.append(element)
print(marks)

# Another way to insert the elements
# student_marks = int(input("Enter the marks of the stduents:"))
# student_mark = student_marks.split()
# print(student_mark)

# sort the marks of the students
for i in range (n-1):
    for j in range (n-1-i):
        if marks[j]>marks[j+1]:
            temp = marks[j]
            marks[j] = marks[j+1]
            marks[j+1] = temp
print(marks)