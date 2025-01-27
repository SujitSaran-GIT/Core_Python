"""
Tuples in python
-----------------
- In Python, a tuple is a built-in data structure that is similar to a list but has some key differences. The most important distinction is that tuples are immutable, meaning that once a tuple is created, its elements cannot be modified, added, or removed.

Key Characteristics of Python Tuples:
-------------------------------------
- Ordered: Like lists, the elements in a tuple have a defined order.
- Immutable: Once a tuple is created, you cannot change, add, or remove elements from it.
- Heterogeneous: A tuple can contain elements of different data types.
- Hashable: Because tuples are immutable, they can be used as keys in dictionaries, unlike lists.
"""
"""
Creating Tuples
---------------
Tuples are created by placing a comma-separated sequence of elements within parentheses ().
Example
-------------
numbers=(1,2,3,4,5,6)
"""
# A tuple of integers
numbers = (1, 2, 3, 4, 5)
#numbers[1]=10               # Error bcz we can't change the index of tuple
print(type(numbers))

# A tuple of strings
fruits = ("apple", "banana", "cherry")

# A mixed tuple
mixed = (1, "apple", 3.14, True)

# A nested tuple
nested_tuple = (1, (2, 3), (4, 5))

# Single element tuple (note the comma)
single_element_tuple = (42,)
"""
Accesing Tuples
-----------------
You can access elements in a tuple using their index, just like you would with a list.
"""
# Accessing the first element
print(fruits[0])  # Output: apple

# Accessing the last element
print(fruits[-1])  # Output: cherry
"""
Common Tuple Operations
------------------------
While tuples are immutable, you can still perform some operations:

Concatenation: You can concatenate two or more tuples using the + operator.
Repetition: You can repeat the elements of a tuple using the * operator.
Slicing: You can access a range of elements using slicing, similar to lists.
Unpacking: You can unpack the elements of a tuple into individual variables.
"""
# Concatenation-: Tuples can be concatenated using + operator
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2  # Output: (1, 2, 3, 4, 5, 6)

# Repetition-: Tuples can be repeated using * opeartor
repeated = tuple1 * 2  # Output: (1, 2, 3, 1, 2, 3)

# Membership-: You can check if the element exists inside the tuple using the in keyword
my_tuple = (10,20,30,40,50)
print(90 in my_tuple)

# Length-: The length of the tuple can be found by len()
print(len(my_tuple))

# Min & Max -: we can find the minimum and maximum element inside the tuple using min() & max()
print(min(my_tuple)," ",max(my_tuple))

# Slicing -: Tuples support slicing to create a new tuple from a subset of the original
sliced = my_tuple[1:4]
print(sliced)

# Unpacking-: Tuples can be unpacked into individual variables
my_tuple = (10,20,30,40,50)
a, b, c= my_tuple
print(a, b, c)
"""
Why Use Tuples?
---------------
Immutability: Tuples are useful when you want to ensure that data cannot be changed, such as in configurations or constants.
Performance: Tuples can be more memory-efficient and faster to access than lists.
Dictionary Keys: Tuples can be used as keys in dictionaries because they are hashable.
"""
