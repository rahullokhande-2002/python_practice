class A:
    team = "india"

    def __init__(self, name, jersey_no):
        self.name = name
        self.jersey_no = jersey_no

    def IPL(self):
        x = "RCB"
        print(self.name, self.jersey_no)

    def IPL2(self):
        print(self.name)
        print(A.team)

obj = A("MS Dhoni", 7)

obj.IPL()
obj.IPL2()
print(A.team)