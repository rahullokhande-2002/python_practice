
class BankAccount:
    def __init__(self,balance:float=0.0)->None:
        self.balance=balance
    def deposite(self,amount:float)->None:
        if amount>0:
            self.balance=self.balance + amount
            print(f"your current blance is ${self.balance} and the despoite ampount is ${amount}")
        else:
              print("enter the  positive value...")           
    def withdraw(self,amount:float)->None:
        if amount>0:
           if self.balance>=amount:
            self.balance=self.balance-amount
            print(f"balance is :",self.balance)
           else:
               print(f"insufficent balance !  ${self.balance}")
        else:
            print("withdraw  amount must be postive")
    
    def check_balance(self):
        print(f"current balance is ${self.balance}")
        


def main()->None:
    account=BankAccount(10000.0)
    while True:
        print("=== Banking System ===")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4.Exit")
        
        choice=input("enter the choice")
        
        if choice=="1":
            
          try:
            amount=float(input("enter the amount for deposite :"))
            account.deposite(amount)
            
          except ValueError:
            print("Enter only value !")
        
           
        elif choice=="2":
            
          try:
            amount=float(input("enter the amount for Withdraw :"))
            account.withdraw(amount)
            
          except ValueError:
            print("Invalid input , Enter only value !")
            
        elif choice=="3":
            account.check_balance()
            
        elif choice=="4":
            print("Exit")
            break
        else:
            print("enter the valid choice")
if __name__=="__main__":
    main()
            
            
 