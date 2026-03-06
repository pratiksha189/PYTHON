# gtyuigbh

print()

'''Q.2 Create an Account class Heirarchy 
Account with super class (acc_id, name, balance)
methods - withdraw and deposit

Create SavingsAccount as sub class of account - additional field (type - personal/corporate etc)
implement withdraw and deposit such that
- maximum upto 1 lakh can be deposited in an account at a time
- Min balance 5000 must be maintained while withdrawal (if type = corporate you withdraw full amount = balance)


Create CurrentAccount as sub class of account
implement withdraw and deposit such that
- maximum upto 2 lakh can be deposited in an account at a time
- Min balance 10000 must be maintained while withdrawal

Create Bank App with Transaction class
Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
These methods will return the new balance after deposite/withdraw

Creare user class with user interface that gives 2 menu options
1. Deposit
2. Withdraw

Both options will ask user to enter money to withdraw/deposite
Display a statement with each transaction and final balance after user exits from the menu


Identify possible Exceptions and implement them'''

from abc import ABC,abstractmethod
class Account(ABC):
    def __init__(self,acc_id, name, balance):
        self._acc_id = acc_id
        self._name=name
        self._balance=balance

    @abstractmethod
    def withdraw(self):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass


class DepositLimitExceed(Exception):
    pass


class MinAmount(Exception):
    pass


class SavingsAccount(Account):
    def __init__(self,personal,corporate,acc_id, name, balance):
        self._personal=personal
        self._corporate=corporate
        super().__init__(acc_id, name, balance)

    def deposit(self,amount):
        if amount>100000:
            raise DepositLimitExceed("maximum upto 1 lakh can be deposited in an account at a time")
        else:
            self._balance=self._balance+amount

    def withdraw(self,amount=None):
        if self._balance<=10000:
            raise MinAmount("Min balance 10000 must be maintained while withdrawal")
        else:
            self._balance=self._balance-amount



