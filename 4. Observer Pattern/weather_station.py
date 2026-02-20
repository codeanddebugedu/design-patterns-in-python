from observer import Observer
from typing import List


class WeatherStation:
    def __init__(self):
        self.__temprature = 0
        self.__observers: List[Observer] = []

    def add_observer(self, new_observer: Observer):
        self.__observers.append(new_observer)

    def remove_observer(self, ob: Observer):
        self.__observers.remove(ob)

    def update_temprature(self, new_temp):
        self.__temprature = new_temp
        self.notify_observers()

    def notify_observers(self):
        for observer in self.__observers:
            observer.update(self.__temprature)
