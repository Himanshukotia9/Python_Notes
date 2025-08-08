# Functions in Python
#Functions are a block of statements that performs a specefic tasks.
"""
# Syntax =>
def func_name(param1, param2,....):
    #some work
    return val

func_name(arg1,arg2,...)
"""

"""
#function defination
def sum(a,b): # a,b are parameters
    s = a+b
    print(s)
    return s

print(sum(5,4)) #5,6 are arguments
# Or
Sum = sum(5,5)
print(Sum)
"""

"""
def print_hello():
    print("hello MF")

print_hello()
print_hello()
print_hello()
print_hello()
"""
"""
# average of 3 numbers

def avg(a,b,c):
    average = (a+b+c)/3
    return average

print(avg(5,7,8))
"""

#default values 
def calc_prod(a=3,b=2):
    prod=a*b
    return prod

print(calc_prod())