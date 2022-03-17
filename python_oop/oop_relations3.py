# Weak relationships

class Customer:

    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.type == "card":
            print("Card type payment")
        elif payment.type == "e-wallet":
            print("E-wallet payment")
        else:
            print("paying by cash")

class  Payment:
    def __init__(self, type):
        self.type = type

pay = Payment("card")

cust1 = Customer("John", 29, 998745)
cust1.purchase(pay)