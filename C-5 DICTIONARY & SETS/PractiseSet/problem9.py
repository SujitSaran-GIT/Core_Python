# Can you change the values inside a list which is contained in set S

s = {8,7,12,"Harry",[1,2]}
print(s)

# Error: No, you cannot include a list in a set in Python because lists are mutable and therefore not hashable. Sets require all their elements to be immutable and hashable. Trying to include a list in a set will raise a TypeError.