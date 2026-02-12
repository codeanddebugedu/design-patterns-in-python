from abc import ABC, abstractmethod


class Workable(ABC):
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    @abstractmethod
    def eat(self):
        pass


class Robot(Workable):
    def work(self):
        print("Robot is working")


class Employee(Workable, Eatable):
    def eat(self):
        print("Employee is eating")

    def work(self):
        print("Employee is working")


e = Employee()
e.eat()
e.work()
