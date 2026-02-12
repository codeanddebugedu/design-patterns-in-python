from account import Account


class FixedDepositAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, current balance = {self.balance}")
