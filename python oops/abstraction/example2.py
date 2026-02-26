# Task 2: Employee Salary System
# Abstract class Employee
# Abstract method → calculate_salary()
# Create:
# FullTimeEmployee
# PartTimeEmployee
# Each calculates salary differently.


from abc import ABC ,abstractmethod
class Employee(ABC):
    
    @abstractmethod
    def calculate_salary(self):
        pass

class FullTimeEmployee(Employee):
    def calculate_salary(self,day,money):
        self.day=day
        self.money=money
        return day*money
    
class PartTimeEmployee(Employee):
    def calculate_salary(self,day,money):
        self.day=day
        self.money=money
        return day*money
        
FT=FullTimeEmployee()
store_ft=FT.calculate_salary(22,1500)
print(store_ft)

PT=PartTimeEmployee()
store_PT=PT.calculate_salary(22,700)
print(store_PT)
    
    