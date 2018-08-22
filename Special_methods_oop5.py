#special methods help us emulate some of the built-in behaviors in python and it also helps us operator overloading
#The next example shows the operator overloading functionality of the '+' operator. Depending on what objects we are working with, the addition has different behaviors
# print(1 + 2)
# print('a' + 'b')


#The special methods are always surrounded by double-underscores which are called dunders.
# Dunder repr and str are implicitly called anytime that we run them on one of our objects
# repr() is an unambiguous representation of an object and should be used for debugging and logging purposes. It is really meant to be seen by other developers
# str() is meant to be a more readable representation of an object and is meant to be used for display to the end-user
# We must atleast have the repr() method because if we have this without an str(), then calling str() on an employee would just use the repr() as the fallback

class Employee:
    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = self.first + "." + self.last + "@company.com"

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    def __str__(self):      #This is more meant for making the output more readable for the end user
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    def __len__(self):
        return len(self.fullname())

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

# print(emp_1)
#Without the repr method we were getting the output as: <__main__.Employee object at 0x7efeff300898>
#But on implementing the repr method, we are getting the output as:Employee('Corey', 'Schafer', 50000)

# print(repr(emp_1))
# print(str(emp_1))
#Withing the above print statements the actual special methods are getting called as below:
# print(emp_1.__repr__())
# print(emp_1.__str__())


#Arithmetic dunder methods
# print(1+2)
#The above operation is actually using the following dunder method:
# print(int.__add__(1,2))

#Strings use their own dunder methods
# print(str.__add__('a', 'b'))


#We can customize how addition act for our objects by creating the dunder add methods
#Now we want to add two employees together and have their result be their combined salaries, then we need to create a dunder add method
# We add the dunder add method in our class above
# print(emp_1 + emp_2)        #If we perform this operation without having our dunder method defined abovem we would have encountered an error


print(len('test'))
print('test'.__len__())
print(len(emp_1))       #This works only after implementing the above dunder method
