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