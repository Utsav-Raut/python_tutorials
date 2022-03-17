class Customer:
    def __init__(self, cust_id, name, age, wallet_balance):
        self.cust_id = cust_id
        self.name = name
        self.age = age
        self.__wallet_balance = wallet_balance

    def update_balance(self, amount):
        if amount > 0 and amount < 10000:
            self.__wallet_balance += amount

    def get_name(self):
        print(f"The name is {self.name}")

    def get_wallet_balance(self):
        print(f"The wallet balance is = {self.__wallet_balance}")

c1 = Customer(100, 'Gopal', 24, 2000)
c1.update_balance(1000)
c1.get_wallet_balance()

c1.name = 'Tom'
c1.get_name()

c1._Customer__wallet_balance = 10000
c1.get_wallet_balance()

