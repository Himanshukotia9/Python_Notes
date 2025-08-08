# Set in Python
# Set is a collection of the unordered items. each elements in the set must be unique & immutable.
#NOTE: Set are always mutable (we can add or remove elements from the set) whereas elements in sets a immutable. 
# List and Dictionary can never be stored in set because they are mutable and can be changed.

"""
Set1 = {1,2,3,4, "Hello", "World", 2,4 ,1}
print(Set1)
print(len(Set1)) # this will ignore the duplicate values because set in python only stores unique values.
print(type(Set1))

set2 = set() # this is how we can create empty set. (Cannot create by saying set2 = {} X wrong way)
print(type(set2))

"""

# Set Methods
set1 = set()
set1.add(1) # this allows us to add values in set
set1.add(2)
set1.add(5)
set1.add(5)
set1.add("Himanshu kotia")
set1.add((1,2,5))
"""set1.add([1,2,5])""" # if we add this line it will give error because we are adding list which is mutable but elements in set cannot be muttable. 

print(set1)

set1.remove(5) # this allows us to remove values from the set
print(set1)

set1.clear() # this will clear all the values in a set or you can say empty the set.
print(len(set1))

set2 = {"Hello", "World", "i", "am", "Himanshu", "Kotia"}

print(set2.pop()) # this will pop/delete a random value from the set 

set3 = {1,2,3,4}
set4 = {3,4,5,6}

print(set3.union(set4)) # this allows us to combine both set values and return new set

print(set3.intersection(set4)) # this allows us to combine common values and return new set

