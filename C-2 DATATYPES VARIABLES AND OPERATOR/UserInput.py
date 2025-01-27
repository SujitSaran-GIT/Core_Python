# user input 

a=input("Enter the first number:")              # 34
print(type(a))                                  # str
b=input("Enter the second number:")             # 45

print("The first number is :",a)                # 34
print("The second number is:",b)                # 45

sum=a+b
print("The sum of the two numbers is:",sum)     # 3445
print("The sum of the two numbers is:",a+b)     # 3445

# we see above that this a string form, to make it integer and find its sum
a=int(input("Enter the first number:"))
print(type(a))                                  # int
b=int(input("Enter the second number:"))
print(type(b))                                  # int

print("The first number is :",a)                # 34
print("The second number is:",b)                # 45

sum=a+b
print("The sum of the two numbers is:",sum)     # 101