class Mobile:
    def __init__(milk, brand, price): #The name of the parameter in this can be anything... instead of 'self' i wrote 'milk'
        print("Inside constructor")
        milk.brand = brand
        milk.price = price

    def purchase(help): #The name of the parameter in this can be anything... instead of 'self' i wrote 'help'
        print("Inside purchase")
        print(f"The brand of the mobile is {help.brand} and it's price is {help.price}")

mob1 = Mobile("Samsung", 25000)
mob1.purchase() #Inbound invocation. Method is called with object reference and the 'self' value does not need to be passed expliciitly

mob2 = Mobile("Apple", 45000)
mob2.purchase()

Mobile.purchase(mob1)   #Outbound invocation. Method is called with class reference and the 'self' value need to be passed expliciitly