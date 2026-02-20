class product:
    def review(self):
        print("product customer review")
class phone(product):
    def __init__(self,price,brand,camera):
        self.price=price
        self.brand=brand
        self.camera=camera
    def buy(self):
        print("buying phone")
class smartphone(phone):
    pass
s=smartphone(2000,"apple",50)
s.buy()
s.review()