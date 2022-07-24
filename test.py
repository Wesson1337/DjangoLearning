from abc import ABC, abstractmethod


class Basic(ABC):
    @abstractmethod
    def hello(self):
        print("Hello from Basic class")


class Advanced(Basic):
    pass


a = Advanced()