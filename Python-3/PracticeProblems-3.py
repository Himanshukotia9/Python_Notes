"""
# Q1) WAP to ask the user to enter names of their 3 favorite movies & store them in a list.
mov1 = input("Enter First : ")
mov2 = input("Enter Second : ")
mov3 = input("Enter Third : ")

movList = []
movList.append(mov1)
movList.append(mov2)
movList.append(mov3)
print(movList)

# Another method => movList.append(input("Enter First : "))
"""

"""
# Q2) WAP to check if a list contains a palindrome of elements. (Hint: use copy() method).

list = [1,2,3,2,1]
#list = ["r","a","c","e","c","a","r"]

list1 = list.copy()
list1.reverse()
if(list == list1):
    print("Palindrome")
else:
    print("NOT Palindrome")
"""

"""
# Q3) WAP to count the number of students with the "A" grade int he following tuple.

tup = ("C", "D", "A", "A", "B", "F", "B", "A")

print(tup.count("A"))
"""

# Q4) Store the above values in a list & sort them from "A" to "F".

grade = ["C", "D", "A", "A", "B", "F", "B", "A"]

grade.sort()
print(grade)