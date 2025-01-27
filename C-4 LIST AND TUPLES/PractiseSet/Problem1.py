# Write a program to store seven fruits in an list entered by the user
fruits = []
# n = int(input("Enter the number of elements in the array:"))

for i in range (7):
    element = input(f"Enter the element {i+1}:")
    fruits.append(element)
print(fruits)

fruits = input("Enter the array elements separted by spaces:")
fruit_array = fruits.split()
print(fruit_array)