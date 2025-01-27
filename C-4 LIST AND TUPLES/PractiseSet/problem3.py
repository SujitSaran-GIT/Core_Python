# Write a sum of a list of Four items
numbers = input("Enter the numbers :")
# split the input into a list of strings
numbers_array = numbers.split()
# convert the list of strings to integers
numbers_array = list(map(int, numbers_array))
print(numbers_array)
t = type(numbers_array[1])
print(t)

# calculate the sum
# total  = sum(numbers_array)
# print(total)
total = 0
length = len(numbers_array)
# calculate the sum using for loop
for i in range (length):
    total+=numbers_array[i]
print(total)