#polymorphism
# 1opeartor overload + , *

#method overloading - same method behave differently
# is not possible => py run code line by line
# def add(a,b):
#     print(a+b)
# def add(a,b,c):
#     return a+b+c
# print(add(2,3,4))



# class bird:
#     def intro(self):
#         print("there are diferent types of birds")
#     def flight(bird):
#         print("most of the birds can fly but some cant fly")
#     class parrot(bird):
#         def flight(self):
#             print("parrot can fly")
#     class penguin(bird):
#         def flight(self):
#             print("pengium can not fly")

# obj1=parrot()
# obj1=intro()
# obj1=flight()




class payment:
    def process_payment(self):
        print("payment processing...")
class UPI(payment):
    def process_payment(self):
         print("payment UPI processing...")
class creditcard(payment):
    def process_payment(self):
         print("payment creditcard processing...")
obj2=creditcard()
obj2.process_payment()













