class BankAccount:
    balance = 0

    def withdraw(self, amount):
        self.balance -= amount

    def deposit(self, amount):
        self.balance += amount

    def get_balance(self):
        return self.balance

B = BankAccount()

while True:
    print("1) Deposit")
    print("2) Withdraw")
    print("3) Balance")
    print("4) Exit")

    op = int(input("Enter an option: "))

    if op == 1:
        amount = int(input("Enter the amount to deposit: "))
        B.deposit(amount)

    elif op == 2:
        amount = int(input("Enter the amount to withdraw: "))
        if amount <= B.get_balance():
            B.withdraw(amount)
        else:
            print("Not enough balance to withdraw")

    elif op == 3:
        print("Balance:", B.get_balance())

    elif op == 4:
        print("Exiting...")
        break

    else:
        print("Invalid option")
