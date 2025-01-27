# If statement
day = "sunday"
if (day == "sunday"):
    print("Today is ",day)

# if-else
age = int(input("Enter the age:"))
if(age>18):
    print("You are eligible to vote here")
else:
    print("You are not eligible to vote")

# elif -: if-else-if
mark = int(input("Enter your mark:"))
if(mark>90):
    print("Topper")
elif(mark>60 and mark<90):
    print("Average")
elif(mark>30 and mark<60):
    print("Normal")
else:
    print("Fail")

'''
Relational Operator / Comparision Operator
---------------------------------------------
# Relationla OPerator are used to evalute conditions inside the if statement. Some examples of relational opeators are:
 == -: Equals
 >= -: Greater than / equal to
 <= -: Lesser than / equal to


Logical Operator
-----------------
In python logical operators are operate on conditional statements
and-: true if both operands are true else false
or-: true if atleast one operand is true or else false
not-: inverts true to false & false to true
'''