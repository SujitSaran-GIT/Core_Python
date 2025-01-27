# Write a program to find out whether a student has passed or failed if it requires a total of 40% and atleast 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user

# take three subjects of marks from user input
marks = []
for i in range(3):
    mark = int(input("Enter the student mark:"))
    marks.append(mark)
total_mark = len(marks) * 100
sum = 0
for i in range(len(marks)):
    sum = sum + marks[i]
percentage = (sum/total_mark)*100
isPassed = False
if percentage>40:
    for i in range(len(marks)):
        if marks[i] < 33:
            isPassed = False
            break
        else:
            isPassed = True
if isPassed == True:
    print("Passed the exam")
else:
    print("Better luck for the next time")