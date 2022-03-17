class Mobile:

    __discount = 50

    def __init__(self, brand, price):
        self.brand = brand
        self.price = price

    def purchase(self):
        self.total = self.price - (self.price * Mobile.__discount / 100)
        print(self.brand, " mobile with price ", self.price, " is available after discount at ",self.total)

    @staticmethod
    def enable_discount():
        Mobile.set_discount(50)

    @staticmethod
    def disable_discount():
        Mobile.set_discount(0)

    @staticmethod
    def get_discount():
        return Mobile.__discount

    @staticmethod
    def set_discount(discount):
        Mobile.__discount = discount

mob1 = Mobile("Asus", 35000)
mob2 = Mobile("Apple", 65000)
mob3 = Mobile("Samsung", 30000)

Mobile.disable_discount()

mob1.purchase()

Mobile.enable_discount()

mob2.purchase()

Mobile.disable_discount()

mob3.purchase()