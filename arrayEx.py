#Give an array of integers , perform the following operations :
#1. insert an element at the end of an array
#2. delete an element from the begining of the  array
#3. search for a specific element in the array 
#4. traverse and print all elements in the array 


my_nums = [11,12,13,14,15,16]

# 1. Insert an element at the end of an array
my_nums.append(17)
print("After insertion:", my_nums)

# 2. Delete an element from the beginning of the array
if my_nums:
    removed_element = my_nums.pop(0)
    print(f"Removed element: {removed_element}")
else:
    print("Array is empty, nothing to remove.")

print("After deletion:", my_nums)

# 3. Search for a specific element in the array
search_item = 14
if search_item in my_nums:
    index = my_nums.index(search_item)
    print(f"Element {search_item} found ")
else:
    print(f"Element {search_item} not found")

# 4. Traverse and print all elements in the array
print("Traversing the array:")
for num in my_nums:
    print(num)