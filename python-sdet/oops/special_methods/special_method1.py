#__str__ helps the print statement to print values when printing an object
class Product:
    def __init__(self,name,price):
        self.name=name
        self.price=price
    def __str__(self):
        return self.name+' '+str(self.price)
p1=Product('Iphone',1000)
print(p1)
