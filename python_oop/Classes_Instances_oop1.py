# class Employee:
#     pass
#
# #Instance variables contain data that are unique for that instance
# emp_1 = Employee()
# emp_2 = Employee()
#
# print(emp_1)
# print(emp_2)
#
# emp_1.first = 'Corey'
# emp_1.last = 'Schafer'
# emp_1.email = 'Corey.Schafer@company.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'Test.User@company.com'
# emp_2.pay = 60000
#
# print(emp_1.email)
# print(emp_2.email)

#######################################################
#The above technique kills the purpose of classes.So we will use the normal method
#here we will use the init method which is like a constructor of Java
#When we create methods within a class they receive the instance as the first argument automatically. By convention we call the instance self. We can call it by any name
#After self we can specify what other arguments that we want
class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

print(emp_1.email)
print(emp_2.email)
# print('{} {}'.format(emp_1.first, emp_1.last))  #This would print the full name but this is requires a lot of typing and is not reusable
print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
