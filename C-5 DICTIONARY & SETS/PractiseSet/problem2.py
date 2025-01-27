# Write a program to input eight numbers from the user and display all the unique numbers(once)
s= set()
for i in range (8):
    num = input("Enter number :")
    s.add(num)
print(s)