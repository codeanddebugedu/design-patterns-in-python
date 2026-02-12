from withdrawable_account import WithdrawableAccount


class SavingsAccount(WithdrawableAccount):
    def __init__(self, amount):
        super().__init__(amount)

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, current balance = {self.balance}")

    def withdraw(self, amount):
        if self.balance < amount:
            print("Cannot withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn, current balance = {self.balance}")
