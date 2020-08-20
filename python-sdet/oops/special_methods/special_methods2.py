# giving definition to '+' operator using __add__ special method
# without defining '+', the addition of the two objects would result in error
class Product:
    counter=100
    def __init__(self,name,description,brand,price):
        Product.counter+=1
        self.id='P'+str(Product.counter)
        self.name=name
        self.description=description
        self.brand=brand
        self.price=price
    def __add__(self,other):
        return self.price+other.price
product1=Product('IPhone','A mobile device with 4GB memory and 64GB Storage space which supprots 4G Network','Apple',72500.25)
product2=Product('Air Max','A Sport Shoe','Nike',1280.0)
print(product1+product2)
