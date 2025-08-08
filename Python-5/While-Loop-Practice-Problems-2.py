"""
# Q1) Print numbers from 1 to 100 using while loop.

i = 1
while i <= 100 :
    print(i)
    i += 1
print("Loop Ended")
"""

"""
# Q2) Print numbers from 100 to 1 using while loop.

i = 100
while i >= 1 :
    print(i)
    i -= 1
print("Loop Ended")
"""

"""
# Q3) Print the multiplication table of number n

x = int(input("Enter a number : "))

i = 1
while i <= 10 :
    print(x, "x", i, "=", x * i)
    i += 1
print("Loop Ended")
"""

"""
# Q4) Print the elements of the following list using loop : [1,4,9,16,25,36,49,64,81,100]

nums = [1,4,9,16,25,36,49,64,81,100]

i = 0
while i < len(nums):
    print(nums[i])
    i += 1
print("Loop Ended")
"""

""""""
# Q5) Search for a number x in this tuple using while loop : [1,4,9,16,25,36,49,64,81,100]

nums = (1,4,9,16,25,36,49,64,81,100)
x = int(input("Enter a number : "))
i = 0

while i < len(nums):
    if(x == nums[i]):
        print("Found the number at index : ", i)
        break
    else: 
        print("Not Found")
    i += 1