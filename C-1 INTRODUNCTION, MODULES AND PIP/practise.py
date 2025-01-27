import random as rd

num = rd.randint(10,20)
print(num)

import math as mt
square = mt.sqrt(25)
print(square)
power = mt.pow(5,5)
print(power)

import pyjokes
joke = pyjokes.get_joke()
print(joke)

# print the multiplication table of 5
for i in range (1,11):
    print(f"5*{i}={5*i}")

# print the multiplication table of a given user input number
number = int(input("Enter the number whose multiplication table is to be calculated:"))

for i in range (1,11):
    print(f"{number}*{i}={number*i}")

# import a library of python to convert text to speech
import pyttsx3 as pyt
engine = pyt.init()
engine.say("Hello sujit what are you doing")
engine.runAndWait()