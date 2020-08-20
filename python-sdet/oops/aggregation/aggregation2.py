class Customer:
    def __init__(self, name, age, phone_no):
        self.name = name
        self.age = age
        self.phone_no = phone_no

    def purchase(self, payment):
        if payment.type == "card":
            print("Payment by card")
        elif payment.type == "e-walllet":
            print("Payment by e-wallet")
        else:
            print("Payment by cash")

class Payment:
    def __init__(self, type):
        self.type = type

c1 = Customer("John", 25, 9887867)
p1 = Payment("card")
c1.purchase(p1)