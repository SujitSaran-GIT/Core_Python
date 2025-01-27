"""
What is list in python?
-----------------------
- In Python, a list is a built-in data structure that is used to store an ordered collection of items. Lists are highly versatile, allowing you to store a sequence of elements, which can be of different data types, such as integers, floats, strings, or even other lists.
- In Python, a list is a collection of items that are ordered and changeable.
- Example
----------
    friends=["apple","akash","rohan",7,false]
    Here apple:str()
         akash:can store value of any datatype
         7:int()
         false:bool()
- Key Characteristics of Python Lists:
---------------------------------------
- Ordered: The elements in a list have a defined order, and this order will not change unless you explicitly modify the list.
- Mutable: You can change the elements of a list after it has been created. This includes adding, removing, or modifying elements.
- Dynamic: The size of a list can grow or shrink as you add or remove elements.
- Heterogeneous: A list can contain elements of different data types.
"""
# Creating a list
#---------------------
# Empty list
my_list = []
print(my_list)

# List with initial elements
my_list = [1, 2, 3, "apple", "banana"]
print(my_list)

# Accesing Elements
#-------------------
# Access the first element
first_item = my_list[0]
print(first_item)

# Access the last element
last_item = my_list[-1]
print(last_item)

# Modifying Elements
#--------------------
# Change the second element
my_list[1] = "orange"
print(my_list[1])

# Adding Elements
#------------------
# Append an item to the end
my_list.append("grape")
print(my_list)

# Insert an item at a specific index
my_list.insert(1, "cherry")
print(my_list)
# Removing Elements
#--------------------
# Remove an item by value
my_list.remove("banana")
print(my_list)

# Remove an item by index
removed_item = my_list.pop(2)
print(removed_item)

# Clear the entire list
my_list.clear()
print(my_list)

# Looping through the list
#---------------------------
my_list = [1, 2, 3, "apple", "banana"]
for item in my_list:
    print(item)

# List Comprehension
#--------------------
# Create a new list with elements that meet a condition
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

# Other Common operations
#------------------------
# Get the length of a list
length = len(my_list)
print(length)

# Check if an item exists in a list
exists = "apple" in my_list
print(exists)

# Sort a list
number=[40,20,30,10,80,60,70]
number.sort()
print(number)

# Reverse a list
number.reverse()
print(number)

friends=["apple","orange",5,5.08,False,"Akash"]
print(friends)
print(friends[4])
print(type(friends[4]))
friends[0]="grapes"
print(friends)
print(friends[1:4])