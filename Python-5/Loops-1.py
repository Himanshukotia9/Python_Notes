# Loops in python
# Loop are used to repeat instruction
# There are 2 types of loops in python : While Loop & For Loop

"""
# While Loop

count = 1
while count<=5 :
    print("Hello, World!")
    count +=  1

# Print 1 to 10 using while loop
i = 1
while i <= 10 :
    print(i)
    i += 1
print("Loop ended")

# Print 9 to 1 using while loop
i = 9
while i >= 1 :
    print(i)
    i -= 1
print("Loop Ended")

# Break Keyword in loop
# It is used to terminate the loop when encountered

i = 1
while i<=5:
    print(i)
    if(i==3):
        break
    i+=1
print("End of Loop")

# Continue Keyword in loop
# It is used to terminate execution in the current iteration & continue execution of the loop with the next iteration

i = 0
while i<= 5:
    if(i==3):
        i+=1
        continue #skip
    print(i)
    i+=1

"""

# For Loop
# For loop are generally used for sequential traversal. For traversing list, string, tuples etc.

"""
list = [1,2,2,4,4,6,6,8,9]

for num in list:
    print(num)

--------------------

veggies = ["Potato", "Tomato", "Capsicum", "Onion"]    

for item in veggies:
    print(item)
"""
"""
tup = (1,5,4,6,2,4,89,2,99)

for num in tup:
    print(num)

--------------------------

name = "Himanshu kotia"
for char in name:
    print(char)

---------------------------

name = "Himanshu kotia"
for char in name:
    if(char == "u"):
        print(char, "Found")
        break # used to break the loop when condition is true
    print(char)
else:
    print("End")
"""

# range()
# Range function returns a sequence of numbers, starting  from 0 by default, and increment by 1 (by default), and stops before a specefic number.
#NOTE Syntax => range(start?, stop, step?)
# here ? means optional
"""
for i in range(1,10,2):
    print(i)
"""

# Pass Statement
# pass is a nul statement thet does nothing. it is used as a placeholder for future code.

for i in range(5):
    pass # used when we dont want to add logic in the block and want to leave it empty fo future use

if i>5:
    pass

print("some usefull work")