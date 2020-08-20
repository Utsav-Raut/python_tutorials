# making a variable private using __ (double underscore)

# class Customer:
#     def __init__(self, cust_id, name, age, wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance
#     def update_balance(self, amount):
#         if amount < 1000 and amount > 0:
#             self.__wallet_balance += amount
#     def show_balance(self):
#         print ("The balance is ",self.__wallet_balance)
# c1=Customer(100, "Gopal", 24, 1000)
# print(c1.__wallet_balance) #This gives, AttributeError: 'Customer' object has no attribute '__wallet_balance'

#Correct way of accessing a private variable outside the class:
# class Customer:
#     def __init__(self, cust_id, name, age, wallet_balance):
#         self.cust_id = cust_id
#         self.name = name
#         self.age = age
#         self.__wallet_balance = wallet_balance
#     def update_balance(self, amount):
#         if amount < 1000 and amount > 0:
#             self.__wallet_balance += amount
#     def show_balance(self):
#         print ("The balance is ",self.__wallet_balance)
# c1=Customer(100, "Gopal", 24, 1000)
# c1._Customer__wallet_balance = 10000000000
# c1.show_balance()

#Error free way of accessing private variables is via getter and setter:
class Customer:
    def __init__(self, id, name, age, wallet_balance):
        self.id = id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance
    def set_wallet_balance(self, amount):
        if amount < 1000 and amount>  0:
            self.__wallet_balance = amount
    def get_wallet_balance(self):
        return self.__wallet_balance
c1=Customer(100, "Gopal", 24, 1000)
c1.set_wallet_balance(120)
print(c1.get_wallet_balance())
