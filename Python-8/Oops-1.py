# OOP in Python
# To map with real world scenarios, we started using objects in code. Thisis called Object Oriented Programming.

"""
# Class & Object in Python
class is a blueprint for creating objects

#creating class
class Student:   #NOTE classname should always start with capital letter
    name = "Karan Kumar"

# creting object (instance)
s1 = Student()
print(s1.name)
"""
"""
class Student:
    name = "Himanshu kotia"

s1 = Student()
print(s1.name)
"""
"""
class Car:
    color = "Blue"
    brand = "Jeep"

c1 = Car()
print(c1.color)
print(c1.brand)
"""

# __init__ Function
# Constructer
# All Classes have a function called __init__(), which is always executed when the class(object) is being initiated.

# Syntax :-> def __init__(self, model):
        # self.model = model
        # print("adding new car in database")
"""
class Car:
    # Default Constructer
    def __init__(self):
        pass
    # Parameterized Constructer
    def __init__(self, model, color):
        self.model = model
        self.color = color #obj attr > class attr
        print("adding new car in database")
    brand = "Jeep"
    color = "Black"
#NOTE :-> Whenever a attribute is present in both class and object importance is always provided to object attribute here color = "Black" will not print instead more importance will always be given to object attribute which is color = "Blue" here

c1 = Car("2025", "Blue")
print(c1.color) #Object.attribute
print(c1.brand) #Class.attribute
print(c1.model) #Object.attribute
print(Car.brand) #Class.attribute

# NOTE :-> the self parameter is the refference to the instanceof the class, and is used to access variable that belongs to the class
"""

# Methods
# Meathods are functions that belong to objects.
"""
class Car:
    def __init__(self, model, color):
        self.model = model
        self.color = color #obj attr > class attr
        print("adding new car in database")
    brand = "Jeep"
    color = "Black"
    def start(self): #this is a method
        print(self.color ,self.brand, "is started")
    
    def get_Model(self):
        return self.model

c1 = Car(2025, "Blue")
c1.start()
print(c1.get_Model())

c1.color = "white" # Can also change value of attributes like this 
c1.start()
"""

# Static Method
#Methods that don't use the self parameters(work at class level)

"""
class Student:
    @staticmethod  #decorators
    def collage():
        print("ABC Collage")

s1 = Student()
s1.collage()
"""
#Decorators allows us to wrap another function in order to extend the behavior of the wrapped function, without permanently modifying it
    