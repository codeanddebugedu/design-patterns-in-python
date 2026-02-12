from abc import ABC, abstractmethod


class Account(ABC):
    def __init__(self, balance):
        self.balance = balance

    @abstractmethod
    def deposit(self):
        pass
