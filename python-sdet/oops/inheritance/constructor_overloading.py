# class Phone:
#     def __init__(self, price, brand, camera):
#         print ("Inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera
#     def buy(self):
#         print ("Buying a phone")
#     def return_phone(self):
#         print ("Returning a phone")
# class FeaturePhone(Phone):
#     pass
# class SmartPhone(Phone):
#     def __init__(self, os, ram):
#         self.os = os
#         self.ram = ram
#         print ("Inside SmartPhone constructor")
#     def buy(self):
#         print("Buying a SmartPhone")
# s=SmartPhone("Android", 2)
# print(s.os)
# print(s.brand) #This throws an error

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
class FeaturePhone(Phone):
    pass
class SmartPhone(Phone):
    def __init__(self, price, brand, camera, os, ram):
        super().__init__(price, brand, camera)
        self.os = os
        self.ram = ram
        print ("Inside smartphone constructor")
    def buy(self):
        print ("Buying a smartphone")
s=SmartPhone(20000, "Samsung", 12, "Android", 2)
print(s.os)
print(s.brand)

