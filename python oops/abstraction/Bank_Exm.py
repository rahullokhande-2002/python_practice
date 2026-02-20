# we cant make the obj of abstract class 
#it is necessary to create the and define abstract method in another so then ot will allowed to inhertie the property

from abc import ABC,abstractmethod
class BankApp(ABC):
    def database(self):
        print("this is database")
    
    @abstractmethod
    def security(self):
        pass

class MobileApp(BankApp):
    def mobilelogin(self):
        print("this is login app")
        
    def security(self):
        print("mobile security")
        
            
obj1=MobileApp()
obj1.database()
obj1.security()