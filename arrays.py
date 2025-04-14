# ARRAYS
"""
= arrays are fundumentals data structures tat stores elements in a contaigous block of memory
= Each element in an array is identified by an index, starting from 0 
=   Arrays provide constant time access to any element using its index

KEY CHARACTERISTICS
= Arrays can have a fixed size or be dynamic
= In strict arrays (Homogenous), all elements must be of the same type, in python's list, they can store elements
 of different types (integers, strings, objects) i.e. Heterogenous
 = Elements are accessed using their index
 = Elements are stored next to each other in the memory(Contigous Memory), allowing fast access but 
 potentially costly when resizing
 = Lists can grow or shrink as needed by using methods like append() or pop()
 = Lists have references to objects, not raw data, so they use more memory than traditional arrays 

 HOW WE CAN IMPIMENT ARRAYS IN PYTHON 
1. Lists : Dynamic, flexible and commonly use as array-like structures
2. Array Modules : Provides a more traditional array with fixed type elements 
3. Numpy Arrays : Specialized for numerical and scientific computing 

"""
# OPERATIONS ON LISTS
"""
= Arrays supports a variety of operations that allow you to manipulate and access data stored within them 
"""
#INITIALIZATION
my_list =[] #empty list
my_list = [1, 2, 3, 4, 5] #list with initial elements 

# ACCESSING ELEMENTS 
"""
= Elements in a list are accessed using their index, which starts at 0(1) -  constant time 

"""
my_list =[2] # 3

# APPENDING ELEMENTS
my_list.append(6) #add 6 to the end of the list

# INSERTING ELEMENTS
"""
= Inserting elements can be done at the beginning, end or any specified index in the array with a time
complexity of O(n)/ Linear Time for insertion at the begining or middle, 0(1)/Constant time for insertionv
at the end (armotized)
"""
my_list.insert(1,1.3) # inserts 1.3 at the index 1 

#DELETING ELEMENTS 
"""
= Deleting can be done from the begining, end  or any specified index in the array with a time
complexity of O(n)/ Linear Time for deletion at the begining or middle, 0(1)/Constant time for deletion from the end 
"""
my_list.pop(1) # remove element at index 1
my_list.pop() # remove last element in the array

#SLICING
my_list[1:3]

#TRAVERSING THE ARRAY/ITERATION
"""
= Traversing involves accessing each element of the array sequentially with a time complexity of 0(n)

"""
my_list = [1, 2, 3, 4, 5] #list with initial elements 


print("Array elements:")
for item in my_list:
    print(item)

#SEARCHING ELEMENTS
"""
= Serching the array can be done using linear search, or binary search(if the array is sorted)
= Time complexity : 0(n) Linear search, 0(log n) Binary search

"""
search_item = 14
if search_item in my_list:
    index = my_list.index(search_item)
    print(f"Element {search_item} found ")
else:
    print(f"Element {search_item} not found")

# PYTHON ARRAY MODULE 
"""
= The array module provides a dynamic array implementation to traditional arrays, enforcing a single data 
type and using less memory than lists 
= It's used for scenarios requering compact storage homogenous data like numerical processing
"""

#CHARACTERISTICS OF PYTHON MODULE
"""
= Elements must be of a specific type, defined type codes

= Arrays are not truly fized but require manual rezizing.
= It stores raw data, not object references, making it memory efficient.
= It supports few operations than lists but it's optimized for basic array tasks,
 """

# TYPE CODES
"""
    'b' = signed char(1 byte)
    'i' = signed int(typically 4 bytes)
    'v' = float(4 bytes)
    'd' = double(8 byte)
"""


