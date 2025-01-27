my_list = [10,"sujit",34.5]
my_list.append("Sumit")
print(my_list)
print(my_list[1])
print(my_list[-1])
# change the 2nd element
my_list[1]="orange"
print(my_list)
# print the full list
for item in my_list:
    print(item)

# reverse a string
my_list.reverse()
print(my_list)
# remove the element using position
my_list.pop(-1)
print(my_list)
# removing the elements
my_list.remove("orange")
print(my_list)