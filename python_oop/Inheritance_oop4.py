class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = self.first + '.' + self.last + '@company.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang

class Manager(Employee):
    def __init__(self, first, last, pay, employees = None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees


    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())

# dev_1 = Employee('Corey', 'Schafer', 50000)
# dev_2 = Employee('Test', 'Employee', 60000)
# print(dev_1.email)
# print(dev_2.email)

#Right now developer class is empty, so Python will walk up the chain of inheritance until it finds what it is looking for. This chain is called the Method Resolution Order
# dev_1 = Developer('Corey', 'Schafer', 50000)
# dev_2 = Developer('Test', 'Employee', 60000)
# print(help(Developer))
# print(dev_1.email)
# print(dev_2.email)
#Both printed the same result even though the Developer class has only pass


#Printing out current Developer's pay
# print(dev_1.pay)
# dev_1.apply_raise()
# print(dev_1.pay)


#Demo of Using super in subclass
dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

# print(dev_1.email)
# print(dev_1.prog_lang)

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])
# print(mgr_1.email)
# mgr_1.add_emp(dev_2)
# mgr_1.print_emps()
#
# mgr_1.remove_emp(dev_1)
# mgr_1.print_emps()


#isinstance() -- Tells us if an object is an instance of a class
print(isinstance(mgr_1, Manager))       #Return True
print(isinstance(mgr_1, Employee))      #Returns True
print(isinstance(mgr_1, Developer))       #Returns False


#and issubclass() -- Tells us if a class is a subclass of another
print(issubclass(Developer, Employee))      #Returns True
print(issubclass(Manager, Employee))      #Returns True
print(issubclass(Manager, Developer))      #Returns True
