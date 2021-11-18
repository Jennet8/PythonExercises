class Budget:
    Balance = 0

    def deposit(self, input):
        self.Balance += input

    def withdraw(self, out):
        self.Balance -= out
    
    def showbalance (self):
        statement = self.Balance
        print(f"Balance is £{statement}.")

food = Budget()

food.deposit(200)

food.withdraw(2.99)

food.showbalance()
