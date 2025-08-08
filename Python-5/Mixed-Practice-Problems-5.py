"""
# Q1) WAP to find sum of first n mumbers (using while)

num = int(input("Enter a number : "))
sum = 0
i=1
while i<=num:
    sum += i
    i+=1
print(sum)
"""

"""
# Q2) WAP to find the factorial of first n numbers. (using for)

n = int(input("Enter a number : "))

fact = 1
for i in range(1,n+1):
    fact *= i
print("Factorial of ", n, " is : ", fact)
"""

"""
# Q3) WAP to print multiplication table of 5

for i in range(1, 11):
    print("5 X ", i, " = ", 5*i)
"""

"""
# Q4) WAP to print all even numbers between 1 to 50

for i in range(1,51):
    if(i%2 == 0):
        print(i)
"""

"""
# Q5) WAP to calculate sum of numbers from 1 to 100

sum = 0
for i in range(1,101):
    sum += i
    i += 1
print(sum)
"""

"""
# Q6) WAP to print each character in the string "Python"

str = "Python"
for char in str:
    print(char)
"""

"""
# Q7) WAP to print first 10 fibonacci numbers
n = 10
a,b = 0,1

for i in range(n):
    print(a)
    a,b = b, a+b
"""

"""
# Q8) WAP to count the number of vowels in a given string

str = "Himanshu kotia"
vowels = "aeiouAEIOU"
count = 0

for char in str:
    if char in vowels:
        count += 1
print("There are ", count, " vowelsin the string")
"""

"""
# Q9) Print the patten 
# *
# **
# ***
# ****

for i in range(1,5):
    print("*" * i)
"""

"""
# Q10) WAP to loop through a list of names and print names longer than 5 characters

list = ["core", "apple", "banana","cat", "hack", "java"]

for item in list:
    if(len(item)>=4):
        print(item)
"""

"""
# Q11) Print numbers from 1 to 10 using while loop

i = 1
while i<=10:
    print(i)
    i += 1
"""

"""
# Q12) print all odd numbers from 1 to 20 using while loop

i = 1
while i<=20:
    if(i%2 != 0):
        print(i)
    i+=1
"""

"""
# Q13) Calculate the sum of digits of a given number

n = int(input("Enter a number : "))

sum = 0
while n>0:
    lstDigit = n % 10
    sum += lstDigit
    n//= 10
print("Sum Of all the digits is : ", sum)
"""

"""
# Q14) Reverse a given number
n = int(input("Enter a number : "))
reversed_num = 0

while n>0:
    digit = n%10
    reversed_num = reversed_num * 10 + digit
    n//=10
print("Reversed number is : ", reversed_num)
"""

"""
# Q15) Keep asking the user to enter a number until they enter 0.
num = int(input("Enter a number : "))
while num!=0:
    print("You Entered ", num)
    num = int(input("Enter a number : "))
print("Congratulations you entered 0. Theprogram has stopped")
"""

"""
# Q16) WAP To Check if a number is palindrome.

num = int(input("Enter a number : "))
original = num
rev_num = 0
while num > 0:
    digit = num % 10
    rev_num = rev_num * 10 + digit
    num //=10
if original == rev_num:
    print(original, " is a palindrome")
else:
    print(original, " is not a palindrome")
"""

"""
# Q17) Generate a number guessing game (loop until correct guess)

import random

random_num = random.randint(1,10)
print(random_num)
num = int(input("Guess a number between 1 to 10 :"))
while num != random_num:
    num = int(input("Guess a number between 1 to 10 :"))
print("you gussed it right")
"""

"""
# Q18) print a count down from a number to 0
import time
num = int(input("Enter a number : "))

while num > 0 :
    print(num)
    time.sleep(1)
    num -=1
print("Times Up!")
"""
"""
# Q19) find the largest digit in a number

num = int(input("Enter a number : "))
list = []
while num>0:
    digit = num%10
    list.append(digit)
    num//=10
print(list)
list.sort(reverse=True)
print(list[0])

--------------------------
num = int(input("Enter a number : ")) # Optimal solution
max_num = 0

while num > 0:
    digit = num % 10
    if digit>max_num:
        max_num = digit
    num//=10
print("Largest Digit is : ", max_num)
"""

# Q20) Simulate a simple login system that allows 3 attempts.

Pass = 'Pass1234'

tries = 3

while tries>0:
    Password = input("Enter the password : ")
    if Pass == Password:
        print("Login Successful")
        break
    else:
        tries -= 1
        if tries > 0:
            print("Wrong Password. ", tries, "Left")
        else:
            print("Login Failed. No attempts left.")