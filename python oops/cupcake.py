# class cupcakes:
#     def ing(self,falv):
#         self.s1="milk"
#         self.s2="sugar"
#         self.s3="water"
#         self.falv=falv
#     def show(self):
#         print(f"the ingertdent is{self.s1} , {self.s2}, {self.s3}")
#         print(f"the falvour is {self.falv}")

# give=cupcakes()
# give.ing("choclate")
# give.show()

# init
class cupcakes:
    def __init__(self,falv):
        self.s1="milk"
        self.s2="sugar"
        self.s3="water"
        self.falv=falv
    def show(self):
        print(f"the ingertdent is{self.s1} , {self.s2}, {self.s3}")
        print(f"the falvour is {self.falv}")

give=cupcakes("cho")
# give.ing("choclate")
give.show()