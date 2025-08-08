# Lists in python
"""
marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks)
print(type(marks))
"""

"""
# 1) Indexing

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
print(marks[2])
print(len(marks))
"""

"""
# 2) Slicing

marks = [94.4, 87.5, 95.2, 66.4, 45.1]
# syntax => list_name[starting_index : ending_index]

print(marks[1:4])
print(marks[-4:-2])
"""

""""""
# List Methods

list = [4,2,7,8,9,4,5]
strList = ["banana", "lichi", "apple"]

list.append(3) # Adds one element at the end 
print(list)

list.sort() # Sorts in ascending order
print(list)

list.sort(reverse=True) # Sorts in descending order
print(list)
strList.sort(reverse=True) # Sorts strings list in descending order
print(strList)

list.reverse() # Reverses List
print(list)

list.insert(5, 10) # Insert element at index. Syntax => list.insert(index,element)
print(list)

list.remove(4) # Removes the first occurrence of element
print(list)

list.pop(4) # Removes element at the given index
print(list)