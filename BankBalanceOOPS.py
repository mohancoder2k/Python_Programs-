class BankAccount:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def deposit(self,amount):
        self.balance+=amount;

    def withdraw(self,amount):
        if(amount<=self.balance):
            self.balance-=amount
        else:
            return "insufficient fund"
    def get_balance(self):
        return f"Account Balance : {self.balance}"
    
account1=BankAccount("John",500);
account1.deposit(500)
account1.withdraw(2000)
print("Balance : ",account1.get_balance())