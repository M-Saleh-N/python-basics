# DATA THYPES IN PYTHON
"""
    NUMERIC DATA TYPES
    float 
    int
    complex

"""

x = 1.2
y = 1 
com = 2 + 3j

#string
msg = "Hello"

#Boolans 
t = True
f = False

#Collection data types
#Mutable -> values can be changed in place
#immutable -> values cannot be changed after creation (you get a new object)
# 1. List - Ordered, Mutable

fruits = ["apple", "banana"]
fruits.append("orange")

#Tuple (Ordered, immutable)
coords = (10,20)

#Dictonary (Key:Value pairs, Mutable)
person = {"name": "Vansh", "age": 17}

#Sets (Unordered, Unique elements)
colors = {"red", "green", "blue"}
colors.add("yellow")

#Type Conversion
#Converting from one data type to another 
#Converting int to str
num = 100.12
numStr = str(num) # "100.12"

#Converting str to int
numInt = int(numStr) # 100.12

#Converting str to float
numFloat = float(numStr) # 100.12

print(numInt)
