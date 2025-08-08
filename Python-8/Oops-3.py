
# NOTE :-> IMPORTANT
# OOPs has 4 major pillars
# 1)Abstraction
# 2)Encapsulation
# 3)Inheritance
# 4)Polymorphism

# 1) Abstraction
# Hiding the implementation details of a class and only showing features to the user.
"""
class Car:
    def __init__(self):
        self.acc = False
        self.brk = False
        self.clutch = False
    def start(self):
        self.clutch = True
        self.acc = False # this is abstraction the process that don't show in the front
        if(self.clutch==True & self.acc == True):
            print("Car started...")
        else:
            print("Engine Failure..")
    
car1 = Car()
car1.start()
"""
 
# 2) Encapsulation
# Wrapping data and functions into a single unit (object)
# It means that the wrapping of all the constructor or functions in a class is called Encapsulation.

# del Keyword
# Used to delete object properties or object itself.

"""
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Himanshu")
print(s1.name)
del s1.name
print(s1.name)
"""

# ------------------------------

# Private (like) attributes & methods
#Conceptual Implementation in python
# Private attribute & method are meant to be used only within the class and are not accessible from outside the class.
# can make any attribute or method private by just adding "__" double underscore before the name.
"""
class Account:
    def __init__(self, acc_no, acc_pass):
        self.acc_no = acc_no
        self.__acc_pass = acc_pass # if we add "__" before a attribute it will become private attribute & will not be accessiable outside class like this pass is not accessiable outside but can be accessed inside like in reset_Pass()
    
    def reset_Pass(self):
        print(self.__acc_pass)

p1 = Account("123456", "Pass123")
print(p1.acc_no)
p1.reset_Pass()
print(p1.__acc_pass)
"""
"""
class Person:
    __name = "anonymous" #not accessable because its private attribute.
 
    def __hello(self): #Also not accessable because its private attribute.
        print("Hello Person!")

    def welcome(self):
        self.__hello()

p1 = Person()
# print(p1.__name)
p1.welcome()
"""

# ------------------------------

# 3) Inheritance
# when one class(child/derived) derives the properties & methods of another class(parent/base)

"""
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car):
    def __init__(self, name):
        self.name = name

car1 = Toyota("Fortuner")
car2 = Toyota("Etios")

print(car1.color)
print(car1.name)
car1.start()
"""
#this is how Toyota class inherited the properties of Car class like start and stop methods.

# Inheritance is of 3 different types:
# A) Single Inheritance
# B) Multi-level Inheritance
# C) Multiple Inheritance

# a) Single Inheritance
# when a single parent class has only one child class its called Single Inheritance.

# b) Multi-level Inheritance
# When a parent class has a child class and that child class has another child class(let's say grand child) which inherits the property of the 1st parent class(Grand Parent) its called Multi-level Inheritance.
# For eg:
"""
class Car:
    color = "Black"
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car):
    def __init__(self, brand):
        self.brand = brand

class Fortuner(Toyota):
    def __init__(self, type):
        self.type = type

car1 = Fortuner("Diesel")
car1.start()
"""
# c) Multiple Inheritance
# When a multiple parent classes have single child classes which inherits the property of parent classes its called Multiple Inheritance.
# For eg:
"""
class A:
    varA = "Welcome to class A"

class B:
    varB = "Welcome to class B"

class C(A,B):
    varC = "Welcome to class C"

c1 = C()
print(c1.varC)
print(c1.varA)
print(c1.varB)
"""

# ------------------------------

# Super Method
# super() method is used to access methods of the parent class
"""
class Car:
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("Car Started...")
    
    @staticmethod
    def stop():
        print("Car Stopped...")

class Toyota(Car):
    def __init__(self, name,type):
        super().__init__(type) # this is how super method is used to get methods of the parent class.
        self.name = name
        super().start()

car1 = Toyota("Fortuner", "electric")
print(car1.type)
"""

# ------------------------------

# Class method
# A class method is bound to the class & receive the class as an implicit first argument.
#NOTE - static method can't access or modify class & generally for utility
"""
class Person:
    name = "anonymos"
    
    # def changeName(self, name):
    #     Person.name = name
        # self.__class__.name = name # this is also an another name to change the class - name attribute.
    
    # correct way to do this above logic is by using class method
    @classmethod #decorator
    def changeName(cls, name): # cls is the keyword for class
        cls.name = name

p1 = Person()
p1.changeName("Himanshu Kotia")
print(p1.name)
"""
# There are 3 types of Methods
# 1) Static Methods (which don't contain any attribute)
# 2) class Methods (which contains cls)
# 3) Instance Methods (which contains self)

# ------------------------------

# Property decorator
# we use @property decorator on any method in the class to use the method as a property.
"""
class Student:
    def __init__(self, phy, chem, math):
        self.phy = phy
        self.chem = chem
        self.math = math

    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3) + "%"

stu1 = Student(91,89,96)
print(stu1.percentage)

stu1.phy = 97
print(stu1.percentage)
"""
# more decorators :-> 1) getter, 2) setter

# ------------------------------

# 4) Polymorphism: operator overloading
# When the same operator is allowed to have different meaning according to the context
"""
print(1+2) #3
print("Himanhu" + " Kotia") #concatenate
print([1,2,3] + [4,5,6]) #merge

# when one operator performs multiple functions or tasks then its called Operator Overloading
""" 