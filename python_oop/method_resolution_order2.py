# Python provides a "__mro__" attribute and "mro()" method to get the resolution order.


# https://www.techbeamers.com/python-multiple-inheritance/

class Appliance:
    def create(self):
        print("Creating class Appliance")

class AC:
    def create(self):
        print("Creating class AC")

class InverterAC(Appliance, AC):
    def __init__(self):
        print("Constructing Inverter AC")

appl = InverterAC()

print(InverterAC.__mro__)
print(InverterAC.mro())