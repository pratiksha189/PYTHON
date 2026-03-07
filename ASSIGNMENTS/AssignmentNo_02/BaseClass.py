from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, acc_id, name, balance):
        self.acc_id = acc_id
        self.name = name
        self.balance = balance

    @abstractmethod
    def deposit(self):
        pass

    @abstractmethod
    def withdraw(self):
        pass