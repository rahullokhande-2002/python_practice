# 🔹 Task 1: Shape Area Calculator
# Create an abstract class Shape
# Abstract method → area()
# Create:
# Circle
# Rectangle
# Each should calculate area differently.

from abc import ABC,abstractmethod
class shape(ABC) :
    @abstractmethod
    def area(self):
        pass
    
    
class  circle(shape):
    def area(self,r):
        self.r=r
        return 3.14 * r*r
    
class rectangle(shape):
    def area(self,l,b):
        self.l=l
        self.b=b
        return (0.5)*1*b
 
  
c=circle()
value_circle=int(input("enter the value of radius : ")) 
area_circle=c.area(value_circle)
print(f"Area of circle {area_circle}")


r=rectangle()
area_rectangle=r.area(22,43)
print(f"area of the rectangle is {area_rectangle}")