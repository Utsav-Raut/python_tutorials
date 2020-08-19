class Product:
    def __init__(self,price,brand):
        self.price=price
        self.brand=brand
    def __del__(self):
        print('Deleting the object')
p1=Product(10000,'Apple')
p2=Product(7000,'Samsung')
del p1
