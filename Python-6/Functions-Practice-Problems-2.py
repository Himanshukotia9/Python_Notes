"""
# Q1) WAF to print the length of a list (list in parameters)
nums = [1,8,6,4,9,2,8,2,46,2,45,95]

def length(list):
    print(len(list))
    return

length(nums)
"""

"""
# Q2) WAF to print the elements of a listin a single line. (list in parameters)

nums = [1,8,6,4,9,2,8,2,46,2,45,95]

def print_list(list):
    i = 0
    while i < len(list):
        print(list[i], end="")
        i+=1
    #for item in list:
        #print(item, end="")
    return

print_list(nums)
"""

"""
# Q3) WAF to find the factorial of n. (n is the parameter)

def fact(n):
    fact = 1
    while n>0:
        fact *= n
        n -= 1
    print(fact)
fact(5)
"""
"""
# Q4) WAF to convert USD to INR

def convert(usd):
    inr = usd * 86.19
    print(inr)
    return
convert(60)
"""

# Q5) WAF to find if a number is odd or even

def odd_even(n):
    if(n%2 == 0):
        print("EVEN")
    else:
        print("ODD")

odd_even(9)
odd_even(6)