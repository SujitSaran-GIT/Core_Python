# Create an empty dictionary. Allow four friends to enter their favorite languages as value and use key as their names. Assume that the names are unique

student_details = {}
for i in range(4):
    name = input("Enter the name of the student:")
    language = input("Enter their choose language:")
    student_details.update({name : language})
print(student_details)