# class NameLengthException(Exception):
#     pass
# class EmployeeIdException(Exception):
#     pass
# class Employee:
#     __trials=0
#     def __init__(self,emp_id,emp_name):
#         self.__emp_name=emp_name
#         self.__emp_id=emp_id
#     def validate_name(self):
#         try:
#             if(len(self.__emp_name) < 4):
#                 Employee.__trials=Employee.__trials+1
#                 raise NameLengthException
#             if( not(self.__emp_id.startswith('E'))):
#                 raise EmployeeIdException
#         except NameLengthException:
#             Employee.__trials=Employee.__trials+1
#             print(Employee.__trials)
#         except EmployeeIdException:
#             Employee.__trials=Employee.__trials+1
#             print(Employee.__trials)
# emp1=Employee('E1001','Tom')
# emp1.validate_name()
# emp2=Employee('1001','Tomy')
# emp2.validate_name()
class InvalidEmployeeException(Exception):
    pass
class Project:
    def __init__(self,employee_list):
        self.__employee_list=employee_list

    def validate_employee(self,employee_id):
        flag=False
        for key in self.__employee_list:
            if(key==employee_id):
                flag=True
        if(flag==False):
            raise InvalidEmployeeException
            print("1")
        return True

project1=Project([1001,1002,1003])
try:
    print(project1.validate_employee(1005))
except Exception:
    print("2")
except InvalidEmployeeException:
    print("3")