'''
What is dictionary in python?
-------------------------------
A dictionary in Python is a collection of key-value pairs that is unordered, mutable, and indexed. It allows you to store and retrieve data efficiently using unique keys.

Key Characteristics of a Dictionary:
---------------------------------------
1. Key-Value Pairs: Each item in a dictionary is a pair of a key and its associated value.
2. Keys Are Unique: Keys in a dictionary must be unique, but values can be duplicated.
3. Mutable: You can add, update, or remove items in a dictionary.
4. Unordered: The order of items in a dictionary is not guaranteed (prior to Python 3.7). Starting with Python 3.7, dictionaries maintain insertion order as an implementation detail.
---------------------------------

Applications of Dictionaries
-------------------------------
1. Storing configuration data (e.g., settings, options).
2. Representing structured data (e.g., JSON objects).
3. Counting occurrences of elements in a dataset.
4. Mapping and lookup operations.

'''
# Creating an empty dictionary
dictionary = {}
marks = {
    "Harry":30,
    "Sujit":50,
    "Sumit":78
}
print(marks)
print(type(marks))
print(marks["Harry"])

# Methods in dictionary
# 1. dict.clear()
# -------------------
# Removes all items from the dictionary, making it empty.
my_dict = {
    "name":"sujit",
    "age":23
}
print(my_dict)
my_dict.clear()
print(my_dict)

# 2. dict.copy()
# ------------------
# Returns a shallow copy of the dictionary.
my_dict = {
    "name":"sujit",
    "age":23
}
new_dict = my_dict.copy()
print(new_dict)

# 3. dict.get(key, default=None)
# Returns the value for a specified key. If the key does not exist, it returns the default value.
print(my_dict.get("name"))
print(my_dict.get("city","Can't find"))

# 4. dict.items()
# Returns a view object containing the dictionary's key-value pairs as tuples.
print(my_dict.items())

# 5. dict.keys()
# Returns a view object containing the dictionary's keys.
print(my_dict.keys())

# 6. dict.values()
# Returns a view object containing the dictionary's values.
print(my_dict.values())

# 7. dict.pop(key, default=None)
# Removes the specified key and returns its value. If the key is not found, it returns the default value.
print(my_dict.pop("name"))
print(my_dict)

# 8. dict.update([other])
# Updates the dictionary with the key-value pairs from another dictionary or an iterable of key-value pairs.
print(my_dict.update({
    "name":"Sujit",
    "city":"Jajpur"
}))
print(my_dict)

# 9. dict.setdefault(key, default=None)
# Returns the value of the specified key. If the key does not exist, it inserts the key with the default value.
print(my_dict.setdefault("name"))
print(my_dict.setdefault("Course"))
print(my_dict)
print(my_dict.update({
    "Course":"MCA"
}))
print(my_dict)

# 10. dict.popitem()
# Removes and returns the last key-value pair as a tuple (LIFO order from Python 3.7 onwards).
print(my_dict.popitem())
print(my_dict)
print(my_dict.update({
    "course":"MCA"
}))
print(my_dict)

# 11. dict.fromkeys(iterable, value=None)
# Creates a new dictionary with the specified keys from an iterable, and all values set to the given value.
keys = ["name","age","city"]
default_keys = dict.fromkeys(keys, "Not Allowed")
print(default_keys)
print(my_dict)

# User input in dictionary
# for dictonary user input you can use a loop to collect key-value pairs from the user

# Initialize an empty dictionary
user_dict = {}

# Get the number of key-value pairs to input
n = int(input("Enter the number of key-value pairs: "))

# Loop to collect keys and values
for _ in range(n):
    key = input("Enter key: ")
    value = input("Enter value: ")
    user_dict[key] = value

print("Your dictionary:", user_dict)
