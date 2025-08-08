"""
# Q1) Write a recursive function to calculate sum of first n natural numbers.

def sum(n):
    if(n==0):
        return 0
    return n + sum(n-1)

print(sum(3))
"""

# Q2) write a recursive function to print all elements in a list. (Hint: use list & index as parameters)

nums = [1,8,6,4,9,2,8,2,46,2,45,95]

def show(list, index=0):
    if(index == len(list)):
        return
    print(list[index])
    show(list, index+1)

show(nums)