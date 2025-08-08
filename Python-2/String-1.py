"""
# escape character

# 1) Next Line
str1 = "this is a string. \nThis represents next line"
print(str1)

# 2) Tab Space
str1 = "this is a string. \tThis represents tab space"
print(str1)
"""

"""
# concatination

str1 = "himanshu"
str2 = "kotia"
print(str1 + str2)
"""

"""
# Length of string

str = "himanshukotia9"
print(len(str))
"""

"""
# indexing

str = "Himanshukotia9"
print(str[12])
"""

"""
# Slicing

# formula => str[startingIndex : endingIndex]
str = 'himanshukotia9'
print(str[8:13])
print(str[:8]) #same as str[0:8]
print(str[8:]) #same as str[8:len(str)] => len(str) is last index
# negative index
print(str[-6:-1])
"""

""""""
# String Functions

str = "Hi i'm Himanshu kotia, a full-stack web developer"
print(str.endswith("er")) # returns true if the string ends with substring "er" else false.
print(str.capitalize()) # capitalize 1st char of the string
print(str.replace("a","@")) # replaces all occurrences of old char with the new one. syntax => str.replace(old,new)
print(str.find("a")) # returns 1st index of 1st occurrer
print(str.count("a")) # counts the occurrence of substring "a"