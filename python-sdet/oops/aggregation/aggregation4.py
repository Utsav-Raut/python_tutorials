#Usage of static attribute
class CustomerCare:
    helpline=111000
class Customer:
    def call_support(self):
        print("Calling ",CustomerCare.helpline)
Customer().call_support()


#Usage of static method
# class CustomerCare:
#     __helpline=111000
#     @staticmethod
#     def get_helpline():
#         return CustomerCare.__helpline
# class Customer:
#     def call_support(self):
#         print("Calling ",CustomerCare.get_helpline())
# Customer().call_support()
