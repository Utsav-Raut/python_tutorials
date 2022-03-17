class Mobile:
    def __init__(self, brand, price):
        print("Inside constructor")
        self.brand = brand
        self.price = price


    def __del__(self): #This is a special method which gets invoked automatically when an object is removed from memory
        print("deleting object")

mob1 = Mobile("Apple", 20000)
print(f"The mobile brand is {mob1.brand} and it's price is {mob1.price}")

mob2 = Mobile("Samsung", 25000)
print(f"The mobile brand is {mob2.brand} and it's price is {mob2.price}")

del mob1 #Although only deletion is called one time on mob1, both mob1 and mob2 gets deleted. mob1 explicitly and mob2 implicitly