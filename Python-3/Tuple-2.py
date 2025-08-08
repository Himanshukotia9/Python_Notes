# Tuples in Python
# A built in data type that lets us create immutable sequence of values.

"""
tup = (1,2,3,1,4,5,4,8)
print(tup[4])
# tup[4] = 6 (not allowed)
"""

"""
#empty tuple
tup = ()
print(tup)
print(type(tup))
"""

"""
#single value tuple
tup = (1,) # for single value tuple always include (,) to be considered as tuple
print(tup)
print(type(tup))
"""
 
 # Tuple Methods

tup = (2,1,3,1,5)
print(tup.index(5)) # Returns index of first occurrence of the element syntax => tup.index(element)
print(tup.count(1)) # Count total occurrences of the element syntax => tup.count(element)