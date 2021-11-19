class Budget:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, input):
        self.balance += input

    def withdraw(self, out):
        self.balance -= out
    
    def showbalance (self):
        statement = self.balance
        print(f"Balance is £{statement}.")

food = Budget(100)
clothes = Budget(25)
house = Budget(10600.45)

food.deposit(200)

food.withdraw(2.99)

clothes.withdraw(30)

food.showbalance()
clothes.showbalance()
house.showbalance()