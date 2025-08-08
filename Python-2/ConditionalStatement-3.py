"""
# If-else statement

age = int(input("Enter Your Age : "))

if(age < 18) :
    print("SORRY, Please try again after", 18 - age, "years")
else :
    print("YES, you can apply for license")
"""

"""
# If-elif-else statement

light = input("enter light color : ")

if(light == "green" or light == "Green" or light == "GREEN"):
    print("Go")
elif(light == "red" or light == "RED" or light == "Red"):
    print("Stop")
elif(light == "yellow" or light == "Yellow" or light == "YELLOW"):
    print("Wait")
else :
    print("Are khena kya chahte hoo")
"""

""""""
# Nested If-else Statement

age = int(input("Enter Your age : "))

if(age >= 18):
    if(age > 70):
        print("Cannot Drive")
    else:
        print("Can Drive")
else:
    print("Cannot Drive")