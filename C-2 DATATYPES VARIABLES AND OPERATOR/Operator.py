# operators in python
"""
- Arithmetic operator: +,-,*,/
- Assignment operator: =,+=,-=
- Comparision operator: ==,>,<,>=,<=,!=
- Logical operators: and, or, not
"""
# Arithmetic operator
"""
 4+5=9
 4 and 5 are operands
 + operator 
 9 result
"""
a=30
b=40
c=a+b
print(c)    # 70

# Assignment operator
"""
a+=4
here += assignment operator
"""
a+=4        # a=a+4  increment the value of a by 4 and then assign to a
print(a)    # 34
a-=4        # a=a-4 Decrement the value of a by 4 and then assign to a
print(a)    #30

# Comparision operator
print(a<b)  # True
print(4>5)  # False
print(a!=b) # True
print(a==b) # False

# Logical operator
"""
AND
----
T T T
T F F
F T F
F F F
"""
print(True and False)   # False
print(True and True)    # True  
print(False and False)  # False
print(False and True)   # False

"""
OR
-----
T T T
T F T
F T T
F F F
"""
print(True or True)     # True
print(True or False)    # True
print(False or False)   # False
print(False or True)    # True

"""
NOT
----
T F
F T
"""
print(not True)         # False
print(not False)        # True