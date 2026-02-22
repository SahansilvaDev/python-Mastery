
from abc import ABC, abstractmethod

# ABC means Abstract Base Class 

class Phone(ABC):
    @abstractmethod
    def call(self):
        print("Calling...")

class SmartPhone(Phone):
    def call(self):
        print("Calling from SmartPhone")

phone1 = SmartPhone()
phone1.call()  # output: Calling from SmartPhone