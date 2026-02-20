# # encapsulatio
# class employee:
#     def __init__(self,name,salary,project):
#         self.name=name
#         self._salary=salary
#         self.__project=project
        
#     def show(self):
#         print(self.name)    
#         print(self._salary) 
#         print(self.__project) 
        
# def subclass(employee):
#     def info(self):
        
#          print(self.name)    
#          print(self._salary) 
#          print(self.__project)      
        

# emp1=subclass("ragh",22222,"ai")
# emp1.info()

    
class ATM:
    def __init__(self,name,name_no,balance):
        self.name=name
        self.name_no=name_no
        self._balance=balance
        self.__pin=1123
    def check(self,enterd_pin):
        if enterd_pin==self.__pin:
            print(self.name)
            print(self.name_no)
            print(self.__pin)
            print(f"balance is : {self._balance}")
                    
        else:
            print("incorrect pin")
atm1=ATM("rahul",243523525,123)
atm1.check(1123)