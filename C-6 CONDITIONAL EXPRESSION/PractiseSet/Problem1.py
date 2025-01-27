# Write a program to find the greatest of four numbers entered by the user

number = []
for i in range(4):
    num = int(input(f"Enter the {i}th number:"))
    number.append(num)
greatest = 0
for i in range(4):
    if(number[i] > greatest):
        greatest = number[i]
if(greatest == 0):
    print(greatest," IS the greatest number")
else:
    print(greatest," Is the greatest number")