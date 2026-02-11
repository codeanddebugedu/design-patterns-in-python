from abc import ABC, abstractmethod


class Notifiable(ABC):

    @abstractmethod
    def send(self):
        pass
