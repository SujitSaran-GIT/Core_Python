# String functions
"""
Some of the mostly used functions to perform oerations or manipulate strings are

1) len() function- This function returns the length of the string
2) String.endswith("rry")- This function tellls whether the variable string ends with the string "rry" or not
   if string is "harry, it returns true for "rry" since harry ends with rry
3) String.count("c)- counts the total number of occurances of any charecter
4) String.capitalize()- This function capitalize the first charecter of a given string
5) String.find(word)- This function finds a word and returns the index of that first occurrance of that word in the string
6) String.replace(old_word,new_word)- This function replace the old word with new word in the entire string
7) String.title()- Capitalize the first charecter of each word in the string
8) String.format()- Formats a string using placeholders
9) String.join()- Joins elements of an iterable into a single string with a specified separator
10) String.split()- Splits a string into a list of substrings based on a specified delimiter(space by default)
11) String.strip()- Removes any leading and trailing whitespace( or specified charecter from a string)
12) String.upper()- Converts all charecer in a string to upper case
13) String.lower()- Converts all charecters in a string to lower case
14) String.str()- Converts an object to a string
"""
name="sujit saran"
print(len(name))                        # 11
print(name.endswith("ran"))             # true
print(name.endswith("suji"))            # false
print(name.startswith("s"))             # true
print(name.startswith("S"))             # false
print(name.capitalize())                # Sujit saran
print(name.count("s"))                  # 2
print(name.find("t"))                   # 4
print(name.replace("saran","sumit"))    # sujit sumit
print(name.title())                     # Sujit Saran
print(name.format(" Sumit"))            
number=345
print(str(number))
print(type(number))                     # int
type_of=str(number)
print(type(type_of))                    # str
print(name.lower())                     # SUJIT SARAN
print(name.upper())                     # sujit saran
print(name.strip())                     # ['sujit','saran']
print(name.split())
fruits=["apple","banana","cherry"]      
print(fruits)                           # ['apple','banana','cherry']
print(", ".join(fruits))                # apple,banana,cherry
print("Name: {}, Fruits:{}".format(name,fruits))
# Name: sujit saran, Fruits: ['apple','banana','cherry']