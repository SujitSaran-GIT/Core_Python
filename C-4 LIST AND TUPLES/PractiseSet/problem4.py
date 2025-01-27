# Write a program to calculate the number of zeros in the following tuple
# (7,0,8,0,0,4,0,3)
# Input tuple elements separated by spaces
user_input = input("Enter the elements of the tuple separated by spaces: ")

# Convert input to a tuple of integers
user_tuple = tuple(map(int, user_input.split()))

# Count the number of zeros in the tuple
count = user_tuple.count(0)

# Print the tuple and the count of zeros
print("Tuple:", user_tuple)
print("Number of zeros in the tuple:", count)
"""
Method	
	5	Description

add(element)	
		Adds an element to the set. If the element is already in the set, it does nothing.

remove(element)
		Removes a specified element from the set. Raises a KeyError if the element does not exist.

discard(element)	
	Removes a specified element from the set. Does not raise an error if the element does not exist.

pop()	
		Removes and returns an arbitrary element from the set. Raises a KeyError if the set is empty.

clear()	
		Removes all elements from the set, leaving it empty.


Method
		Description

union(other_set)	
		Returns a new set containing all elements from both sets (equivalent to `A

intersection(other_set)	
		Returns a new set containing only the elements common to both sets (equivalent to A & B).

difference(other_set)	
		Returns a new set with elements in the first set but not in the second set (equivalent to A - B).

symmetric_difference(other_set)	
		Returns a new set with elements in either set but not in both (equivalent to A ^ B).


Method	Description
isdisjoint(other_set)	Returns True if the two sets have no common elements.
issubset(other_set)	Returns True if the current set is a subset of the other set (all elements in the first set exist in the second).
issuperset(other_set)	Returns True if the current set is a superset of the other set (contains all elements of the other set).


Method
		Description

update(other_set)
		Adds all elements of other_set to the current set (equivalent to `A

intersection_update(other_set)	
		Updates the set, keeping only elements found in both sets (equivalent to A &= B).

difference_update(other_set)	
		Updates the set, removing elements found in the other set (equivalent to A -= B).

symmetric_difference_update(other_set)	
		Updates the set, keeping only elements found in either set but not both (equivalent to A ^= B).


Method
	Description

copy()	
		Returns a shallow copy of the set.


"""