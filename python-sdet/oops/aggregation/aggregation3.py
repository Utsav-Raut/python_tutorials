class Customer:
    def __init__(self, name, cust_type, bill):
        self.name = name
        self.cust_type = cust_type
        self.bill = bill
    
    def calculate_bill(self):
        tax1 = Tax(self.cust_type)
        total_bill = self.bill * tax1.calculate_tax()
        return total_bill

class Tax:
    def __init__(self, cust_type):
        self.cust_type = cust_type
    
    def calculate_tax(self):
        if self.cust_type == "Student":
            return 5
        else:
            return 10

c1 = Customer("John", "Student", 100)
print(c1.calculate_bill())
