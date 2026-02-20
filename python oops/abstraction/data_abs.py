# data abstraction  ===> hiding all implention from end user
# how to acheive abstractions
#1 

from abc import ABC,abstractclassmethod
# class myclass:
#     def study(self):
#         print("i am studying")
# obj=myclass()
# obj.study()


# class myclass(ABC):
#     def study(self):
#         print("i am studying")
        
#     @abstractclassmethod
    
#     def mock(self):
#         pass
# obj=myclass()
# obj.study()]]


from abc import ABC, abstractmethod

class BankApp(ABC):
    
    def database(self):
        print("this is database")
    
    @abstractclassmethod
    def security(self):
        pass
    
    @abstractclassmethod
    def display(self):
        pass


class MobileApp(BankApp):
    
    def mobile_login(self):
        print("login into mobile")
    
    def security(self):   # must implement abstract method
        print("security system active")
    
    def display(self):
        print("display")


o1 = MobileApp()
o1.mobile_login()
o1.display()
o1.security()


