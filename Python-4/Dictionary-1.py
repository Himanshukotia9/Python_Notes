# Dictionary in Python
# Dictionaries are used to store key:value pairs. They are unordered, mutable(changeable) & don't allow duplicate keys 

"""
info = {
    "name" : "Himanshu",
    "age" : 23,
    "skills": ["JavaScript", "React", "Node", "Express.js", "MongoDB", "Firebase"],
    "is_employed" : True,
}

print(info)
print(type(info))

print(info["skills"]) # Allows us to print values
info['age'] = 24 # Allows us to change values
print(info["age"])
info["surname"] = "Kotia" # Allows us to add new key value pair
print(info)
"""

# If a new key value pair is created with the same key it will not create a new one but instead overwrite the existing one

"""
null_Dict = {} # This will create a enpty dictionary
null_Dict["name"] = "HimanshuKotia9"
print(null_Dict)
"""

"""
# Nested Dictionaries

student = {
    "name" : "Himanshu",
    "Score" : {
        "Python" : 67,
        "Oops programming" : 82,
        "DSA" : 54,
    }
}

print(student)
print(student["Score"]["DSA"])
"""

# Dictionary Methods

student = {
    "name" : "Himanshu",
    "Score" : {
        "Python" : 67,
        "Oops programming" : 82,
        "DSA" : 54,
    }
}

print(student.keys()) # Print all the keys in the dictionary
print(student["Score"].keys())

print(len(student)) # Prints the number of keys 
print(len(list(student.keys())))

print(list(student.values())) # prints all the values in the dictionary. list() is optional but converts values into list.

print(student.items()) # Returns all (key, value) pairs as tuples
pairs = list(student.items())
print(pairs[0])

print(student["name"]) # Returns the value of the key but gives an error if key is not found
print(student.get("name2")) # This also returns the value of key but doesn't return an error if key is not found and returns None

student.update({"city" : "Jalandhar"}) # Allows us to Update Dictionary if the key is not present it will create a new key value pair, if it is already existing it will update the value and replace old with new value
print(student)
new_Dict = {
    "name" : "Himanshu Kotia"
}
student.update(new_Dict)
print(student)

