#Practice Problems
"""
# Q1) Store The Following word meaning in a python dictionary: 
# table: "a piece of furniture", "list of facts and figures"
# cat: "a small animal"

dict = {
    "table": ["a piece of furniture", "list of facts and figures"],
    "cat" : "a samll animal"
}

print(dict)
"""

"""
# Q2) You are given a list of subjects for students. Assume one Classroom is required for 1 subject how many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"

subjects = {"python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"}
print(len(subjects))
print(subjects)
"""

"""
# Q3) WAP to enter marks of 3 subjects from the user and store them in a dictionary. start with an empty dictionary & add one by one. use subject name as key & marks as value.
report = {}
x= int(input("Marks obtained in Physics : "))
y= int(input("Marks obtained in Chemistry : "))
z= int(input("Marks obtained in Maths : "))

report.update({"Physics": x})
report.update({"Chemistry": y})
report.update({"Maths": z})

print(report)
print(type(report))
"""

""""""
# Q4) figure out a way to store 9 & 9.0 as seperate values in a set (you can take help of built-in data types)

set1 = {
    ("float", 9.0),
    ("int", 9)
}
print(set1)