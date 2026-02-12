from abc import ABC, abstractmethod


class BankAccount(ABC):
    def __init__(self, balance: int):
        self.balance: int = balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self):
        pass


class SavingsAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        if self.balance < amount:
            print("Cannot withdraw, not enough balance")
        else:
            self.balance -= amount
            print(f"Amount withdrawn, remaining balance {self.balance}")

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, remaining balance {self.balance}")


class FixedDepositAccount(BankAccount):
    def __init__(self, balance):
        super().__init__(balance)

    def withdraw(self, amount):
        raise Exception("Cannot withdraw from FD")

    def deposit(self, amount):
        self.balance += amount
        print(f"Amount deposited, remaining balance {self.balance}")


# s = SavingsAccount(1000)
# s.deposit(1000)
# s.withdraw(1500)

fd = FixedDepositAccount(1000)
fd.deposit(1000)
fd.withdraw(500)
