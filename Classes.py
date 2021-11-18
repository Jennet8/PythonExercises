class Budget:
    Balance = 0

    def deposit(self, input):
        self.Balance += input

    def withdrawal(self, out):
        self.Balance -= input
    
    def showbalance (self):
        return self.Balance

food = Budget()
