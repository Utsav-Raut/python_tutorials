# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)        #We could have done Employee.raise_amount. Class vars can be accessed through the class itself or an instance of the class
#
#     @classmethod            #This annotation makes a regular method as a class method
#     def set_raise_amt(cls, amount):     #Here we have the class as our first argument as opposed to our instance methods which have the instance as the first argument
#         cls.raise_amount = amount
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)
#
# # Employee.set_raise_amt(1.05)        #We are setting the class variable set_raise_amt
# # #We could have done as: Employee.raise_amount = 1.05. But now we are using the class method instead
# #
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)
#
#
# #WE can run class methods from instances as well, but that is not a common practice
# #Doing so will still change the class variable and set the value accordingly
# #The following code prints the same output as above
# # emp_1.set_raise_amt(1.05)
# # print(Employee.raise_amount)
# # print(emp_1.raise_amount)
# # print(emp_2.raise_amount)
#
#
# #Class methods as alternative constructors- It means we can use the class methods to provide multiple ways of creating our objects
# #Someone using our above employee class has a few specific use cases where the person is getting employee info in the form of a string that is separated by hifens and the person is constantly needing to parse the string before creating new Employees
# #Is there any way to pass in a string and create an Employee from that? Example is below:
# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'
# #To create a new employee from our string we need to do the following:
# first, last, pay = emp_str_1.split('-')
# new_emp_1 = Employee(first, last, pay)
# print(new_emp_1.email)


#If this is a common use case of how someone is using our class then we don't want them to parse the strings everytime that they want to create a new employee
#So we create an alternative constructor that allows them to pass the string and we can create the employee for them
# class Employee:
#
#     num_of_emps = 0
#     raise_amount = 1.04
#
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#         Employee.num_of_emps += 1
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)        #We could have done Employee.raise_amount. Class vars can be accessed through the class itself or an instance of the class
#
#     @classmethod            #This annotation makes a regular method as a class method
#     def set_raise_amt(cls, amount):     #Here we have the class as our first argument as opposed to our instance methods which have the instance as the first argument
#         cls.raise_amount = amount
#
#     #This is our alternative constructor
#     @classmethod
#     def from_string(cls, emp_str):
#         first, last, pay = emp_str.split('-')
#         return cls(first, last, pay)            #This line is going to create the new employee by using the class variable instead of Employee because now they are the same thing.

# emp_str_1 = 'John-Doe-70000'
# emp_str_2 = 'Steve-Smith-30000'
# emp_str_3 = 'Jane-Doe-90000'

# new_emp_1 = Employee.from_string(emp_str_1)
# print(new_emp_1.email)
# print(new_emp_1.pay)


#STATIC METHODS:

#When working with classes regular methods automatically passes the instance as the first argument and we call that 'self'
#Class methods automatically passes the 'class' as the first argument and we call that 'cls'
#Static methods do not pass anything automatically. It behave as regular functions except we include them in our classes because they have some logical connection with the class

class Employee:

    num_of_emps = 0
    raise_amount = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
        Employee.num_of_emps += 1

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)        #We could have done Employee.raise_amount. Class vars can be accessed through the class itself or an instance of the class

    @classmethod            #This annotation makes a regular method as a class method
    def set_raise_amt(cls, amount):     #Here we have the class as our first argument as opposed to our instance methods which have the instance as the first argument
        cls.raise_amount = amount

    #This is our alternative constructor
    @classmethod
    def from_string(cls, emp_str):
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)            #This line is going to create the new employee by using the class variable instead of Employee because now they are the same thing.

    @staticmethod
    def is_workday(day):                        #In python, dates have the weekday methods where Monday = 0 and Sunday = 6 and all the other days in between
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

    #THE BIGGEST GIVEAWAY THAT A METHOD SHOULD BE A STATIC METHOD IS IF WE DON'T ACCESS THE INSTANCE OR THE CLASS ANYWHERE WITHIN THE FUNCTION

import datetime
my_date = datetime.date(2016, 7, 10)
print(Employee.is_workday(my_date))
