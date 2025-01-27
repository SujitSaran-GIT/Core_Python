# TypeFunction() and TypeCasting()

"""
type() function is used to find the data of a given variable in python
"""
a=1                     # a is an integer
b=3
print(type(a),type(b))
str="Sujit"             # str is a string 
print(type(str))
flo=22.4                # flo is a floating number
print(type(flo))
flo="22.4"
print(type(flo))
boolean=True               # bool is an boolean type value
print(type(boolean))
non=None                # non is a none type variable
print(type(non))

# Conversion of floating string value to float 
"""
 Above we can clearly see in line 13 that the type of flo is string instead of float now we convert the value of ths string to float
"""
flot=float(flo)
print(flot)         # 22.4
print(type(flot))   # Float