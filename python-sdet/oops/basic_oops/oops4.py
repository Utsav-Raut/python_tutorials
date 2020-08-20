class Mobile:
    def __init__(self):
        print("Inside constructor")
    def purchase (self):
        print("Purchasing a mobile")
mob1=Mobile()
mob1.purchase() #Inbound method invocation, We need not pass the value for self.
Mobile.purchase(mob1) #Outbound method invocation, We have to pass the object as the value of self.
