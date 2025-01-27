"""
What is sets in python
-----------------------
In Python, a set is a built-in data type that represents an unordered collection of unique items. Sets are useful when you want to store multiple items and ensure that each item is distinct. They are similar to mathematical sets and support many operations like union, intersection, and difference.

Key Features of Sets:
------------------------------
Unordered: The items in a set are not stored in any particular order.
Unique: A set automatically removes duplicate elements.
Mutable: You can add or remove elements from a set, but the elements themselves must be immutable (e.g., numbers, strings, tuples).
"""
# Creating a empty sets
# sets = {} error
sets = set()
# Creating a set 
fruits = {"apple",35,50.7}
print(fruits)
# adding elements inside the sets
sets.add(1)
sets.add(2)
print(sets)
# removing an element from the list
sets.remove(2)
print(sets)
sets.add(2)
print(sets)

"""
Common Set Operations:
---------------------------
Union (| or union()): Combines elements from both sets.
Intersection (& or intersection()): Finds common elements.
Difference (- or difference()): Finds elements in one set but not the other.
Symmetric Difference (^ or symmetric_difference()): Finds elements in either set but not in both.
"""
A = {10,20,30,40,50}
B = {30,40,50,60,70}
print(A | B)    #Union
print(A & B)    #Intersection
print(A-B)      #Difference
print(A^B)      #Symmetric Difference
# {70, 40, 10, 50, 20, 60, 30}
print(A)

"""
In sets if i create a set after run the program the elements inside set is scttered why
----------------------------------------------------
In Python, sets are unordered collections, meaning they do not maintain any specific order for the elements you add. This is different from other collections like lists, which maintain the order in which elements are inserted.

Why are the elements "scattered" in a set?
----------------------------------------------

Unordered Nature: The internal structure of a set uses a hash table, which allows for efficient lookups, additions, and removals of elements. However, this structure does not guarantee that the elements will be stored or retrieved in any particular order. This is why when you print a set, the order of elements might seem "scattered" or random.

Hashing: When elements are added to a set, they are hashed (converted into a unique numerical value) to determine their position in the set. This means the set doesn’t care about the order in which you insert elements but ensures that each element is unique. The result is that the internal ordering is based on these hash values, which can seem "scattered."
"""
# Example
my_set = {10,20,30,40,50}
# When we print this we expect that the output will be {10,20,30,40,50}
print(my_set)
# But the output is {40,10,50,30,20} in a unordered format

# Set Methods in python
# In Python, sets have several built-in methods that provide functionality for performing various operations like adding, removing, or checking elements and performing set operations.
"""

In Python, sets have several built-in methods that provide functionality for performing various operations like adding, removing, or checking elements and performing set operations.

Here’s a detailed list of set methods:

1. Adding and Removing Elements

"""
# 1. Adding and Removing Elements
s = {1,2}
# s.add(element)
s.add(3)
print(s)

# s.remove(element)
s.remove(3)
print(s)
# s.remove(4)
# print(s)          Exception

# 2. Update -: Adds multiple elements to the set from an iterable (list, tuple, etc..)
s.update([3,4,5,6])
print(s)

# 3. discard(element)-: Removes the specified element if it exists. Does not raise an error if the element is not found
s.discard(8)
print(s)

# What is the difference between remove() and discard()
# Ans
# Both are having same functionality to remove an element from the set but the difference is that if we use remove(element) method and the element is not found then it will throw an exception but in case of discard(element) if the element is not found it will not throw an exception

# 4. pop(element)-: Removes element froom the first and returns an erbitary element from the set. Raises a keyerror if the set is empty
s.pop()
print(s)

# 5-: clear()-: Removes all element from the set
s.clear()
print(s)

# SET OPERATIONS
# ----------------
# 1. union(other_set) : Returns a new set with all elements from both sets.
set_one = {1,2,3,4,5}
set_two = {5,6,7,8,9,10}
print(set_one.union(set_two))

# 2. Intersection : Returns a new set with elements common to both sets.
print(set_one.intersection(set_two))

# 3. difference : Returns a new set with elements in the first set but not in the second.
print(set_one.difference(set_two))

# 4. symmetric_difference(other_set): Returns a new set with elements in either set but not in both.
print(set_one.symmetric_difference(set_two))

# Comparison and Membership
# ---------------------------
# 1. issubset(other_set) : Checks if the set is a subset of another set.
first_set = {1,2,3,4,5,6,7,8,9,10}
second_set = {6,7,8,9,10,11,12,13,14,15}
third_set = {6,7,8,9,10}
print(first_set.issubset(second_set))
print(third_set.issubset(second_set))

# 2. issuperset(other_set) : Checks if the set is a superset of another set.
print(first_set.issuperset(third_set))
print(third_set.issuperset(first_set))

# 3. isdisjoint(other_set) : Checks if two sets have no elements in common.
fourth_set = {1,2,3,4,5}
fifth_set = {6,7,8,9,10}
print(fourth_set.isdisjoint(fifth_set))
print(third_set.isdisjoint(first_set))

# 4. copy() : Returns a shallow copy of the set.
sets = {1,2,3}
sets_copy = sets.copy()
print("sets_copy:",sets_copy)