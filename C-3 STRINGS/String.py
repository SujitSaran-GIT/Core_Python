# strings in python
"""
- String is a datatype in python
- Strign is a sequence of charecters enclosed in quotes
- String i s immutable
- We can primarily write a string in these three ways
a='harry'
a="harry"
a='''harry'''
"""
a='harry'
print(a)
a="harry"
print(a)
print(id(a))

# String slicing
"""
- A string in python can be slices for getting a part of the strings
        H   A   R    R    Y
        0   1   2    3    4         length=5
        => Counting from left to right
        -5  -4  -3  -2   -1
        <= Counting from right to left
"""
print(len(a))

"""
The index in a string starts from 0 to length-1 in python. 
In order to slice a string we use the following syntax:
    s1=name[index_start:index_end]
    index_start-first index included
    index_end- last index is not included
"""
print(a[0:3])   # Start from index 0 all the way till 3(Excluding 3)
print(a[1:3])   # Start from index 1 all the way till 3(Excluding 3)
print(a[1])     # a
print(a[-1])    # y
print(a[-4:-1]) # arr
print(a[1:4])   # arr
print(a[0:4])   # harr print(a[0:4]) is same as print(a[:4])
print(a[:4])    # harr
print(a[1:])    # arry print(a[1:]) is same as print(a[1:5])
print(a[1:5])   # arry