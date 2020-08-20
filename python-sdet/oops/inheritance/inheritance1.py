#accessing private data members through getters and setters

class Phone:
    def __init__(self, price, brand, camera):
        print ("Inside phone constructor")
        self.__price = price
        self.brand = brand
        self.camera = camera
    def buy(self):
        print ("Buying a phone")
    def return_phone(self):
        print ("Returning a phone")
    def get_price(self):
        return self.__price
    def set_price(self,price):
        self.__price=price
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def check(self):
        print(self.get_price())
s=SmartPhone(20000, "Apple", 13)
s.check()
