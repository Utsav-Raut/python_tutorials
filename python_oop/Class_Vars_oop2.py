# Class vars are vars that are shared among all instances of a classself.
# While instance vars can be unique for each instance like name, email, pay, class variables are shared for each instance
# class Employee:
#
#     raise_amount = 1.04
#     def __init__(self, first, last, pay):
#         self.first = first
#         self.last = last
#         self.pay = pay
#         self.email = first + '.' + last + '@company.com'
#
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)
#
#     def apply_raise(self):
#         self.pay = int(self.pay * self.raise_amount)        #We could have done Employee.raise_amount. Class vars can be accessed through the class itself or an instance of the class
#
# emp_1 = Employee('Corey', 'Schafer', 50000)
# emp_2 = Employee('Test', 'User', 60000)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)
#The instances do not have the attribute raise_amount themselves but they access the class's raise_amount attribute
#This can be shows as below:
# print(emp_1.__dict__)       #This will show the attributes of emp_1, this will not contain raise_amount
# print(Employee.__dict__)    #This will show the attributes of the class and it will contain raise_amount


# Employee.raise_amount = 1.05        #This will change raise amout for the entire class and thus will get reflected in all the instance vars as well
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)

# emp_1.raise_amount = 1.05           #This will change raise_amount for emp_1 only
# print(emp_1.__dict__)               #Now emp_1 has now raise_amount in it's namespace and it is equal to 5%
# print(Employee.raise_amount)
# print(emp_1.raise_amount)
# print(emp_2.raise_amount)


#Now we want to keep track of all Employees

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

print(Employee.num_of_emps)
emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)
print(Employee.num_of_emps)
