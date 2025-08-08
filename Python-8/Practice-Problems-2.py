# Q1) Create student class that takes name & marks of 3 subjects a arguments in constructor. then create a method to print the average.
"""
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    
    def calc_Avg(self):
        total = 0
        for mark in self.marks:
            total += mark
        avg = total / len(self.marks)
        return avg

s1 = Student("Himanshu", [78,86,91])
print(s1.name)
print(s1.marks)
print(s1.calc_Avg())
"""

# Q2) Create an Account class with 2 attribute - balance & account no. . Create method for debit, credit & printing the balance

"""
class Account:
    def __init__(self, balance, accountNo):
        self.balance = float(balance)
        self.accountNo = accountNo
        print("Balance of", self.accountNo, "account no. is", self.balance, "Rs")

    def debit(self, debit):
        self.balance -= debit
        print("Account no.", self.accountNo, "debited with", float(debit), "Rs")
        print("Available Balance is", self.balance)
    
    def credit(self, credit):
        self.balance += credit
        print("Account no.", self.accountNo, "credited with", float(credit), "Rs")
        print("Available Balance is", self.get_Bal())

    def get_Bal(self):
        return self.balance
    
acc1 = Account(5264, 8283020999)
acc1.debit(52)
acc1.credit(51)
"""

# Q3)