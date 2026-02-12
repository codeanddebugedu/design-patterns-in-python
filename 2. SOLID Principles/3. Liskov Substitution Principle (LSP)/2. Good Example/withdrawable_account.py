from account import Account
from abc import abstractmethod


class WithdrawableAccount(Account):
    def __init__(self, balance):
        super().__init__(balance)

    @abstractmethod
    def withdraw(self, amount):
        pass
