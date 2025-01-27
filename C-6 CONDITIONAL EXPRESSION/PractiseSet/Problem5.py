# Write a program which finds out whether a given name is present in a list or not

my_list = ["SUJIT","SUMIT","BIRAJA","MANISHA"]
name = input("Enter your name:")
for i in range(len(my_list)):
    if my_list[i] == name:
        print("Successfully name found")
        break

if(name in my_list):
    print("Your name is in the list")
else:
    print("We can't found your name")