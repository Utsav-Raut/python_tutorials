class Customer:
    def __init__(self, name, cust_type, bill):
        self.name = name
        self.cust_type = cust_type
        self.bill = bill

    def calculate_bill(self):
        tax1 = Tax(self.cust_type)
        self.total = self.bill * tax1.tax_details(self.cust_type)
        return self.total

class Tax:
    def __init__(self, cust_type):
        self.cust_type = cust_type
    
    def tax_details(self, cust_type):
        if self.cust_type == "student":
            tax = 5
        else:
            tax = 10
        return tax

cust1 = Customer("Roger", "Student", 600)
print(cust1.calculate_bill())