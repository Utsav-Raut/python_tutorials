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

    @classmethod            #This annotation makes a method as a class method
    def set_raise_amt(cls, amount):     #Here we have the class as our first argument as opposed to our instance methods which have the instance as the first argument
        cls.raise_amount = amount

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'User', 60000)

Employee.set_raise_amt(1.05)        #We are setting the class variable set_raise_amt
#We could have done as: Employee.raise_amount = 1.05. But now we are using the class method instead

print(Employee.raise_amount)
print(emp_1.raise_amount)
print(emp_2.raise_amount)
