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
    def withdraw(self,amount):
        pass

    @abstractmethod
    def deposit(self,amount):
        pass
    def __str__(self):
        return f'{self._name},{self._balance}'

class DepositLimitExceed(Exception):
    pass


class MinAmount(Exception):
    pass


class SavingsAccount(Account):
    def __init__(self,account_type,acc_id, name, balance):
        self._account_type=account_type
        super().__init__(acc_id, name, balance)

    def deposit(self,amount):
        if amount>99999:
            raise DepositLimitExceed("maximum upto 1 lakh can be deposited in an account at a time")
        else:
            self._balance=self._balance+amount
            return self._balance

    def withdraw(self,amount):
        if self._balance-amount<=10000:
            raise MinAmount("Min balance 10000 must be maintained while withdrawal")
        else:
            self._balance=self._balance-amount
            return self._balance

class Personal(Account):
    def __init__(self,acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def withdraw(self,amount):
        if self._balance-amount<=5000:
            raise MinAmount("Min balance 10000 must be maintained while withdrawal")
        else:
            self._balance=self._balance-amount
            return self._balance

    def deposit(self,amount):
        if amount>99999:
            raise DepositLimitExceed("maximum upto 1 lakh can be deposited in an account at a time")
        else:
            self._balance=self._balance+amount
            return self._balance

class CurrentAccount(Account):
    def __init__(self,account_type,acc_id, name, balance):
        self._account_type=account_type
        super().__init__(acc_id, name, balance)

    def deposit(self,amount):
        if amount>199999:
            raise DepositLimitExceed("maximum upto 1 lakh can be deposited in an account at a time")
        else:
            self._balance=self._balance+amount
            return self._balance

    def withdraw(self,amount):
        if self._balance-amount<=10000:
            raise MinAmount("Min balance 10000 must be maintained while withdrawal")
        else:
            self._balance=self._balance-amount
            return self._balance
# e1=SavingsAccount(101,"prati",4000,400000)
# print(e1.deposit(100000))
# e2=SavingsAccount(101,"prati",4000,400000)
# print(e2.withdraw(2000))

# e3=Personal(103,"ashish",567889)
# print(e3.withdraw(6000))


# e3=CurrentAccount("current",101,"vijay",98765)
# print(e3.withdraw(90000))

'''
Create Bank App with Transaction class
Create Method withdraw_from_account(account : Account)  and deposit_to_account(account : Account)
These methods will return the new balance after deposite/withdraw

Creare user class with user interface that gives 2 menu options
1. Deposit
2. Withdraw

Both options will ask user to enter money to withdraw/deposite
Display a statement with each transaction and final balance after user exits from the menu


Identify possible Exceptions and implement them'''


class Transaction:
    def __init__(self,acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def withdraw_from_account(account : Account):
        pass
    def deposit_to_account(account : Account):
        pass



class User(Transaction):
    def __init__(self,acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def deposit_to_account(self,amount):
        if amount>199999:
            raise DepositLimitExceed("maximum upto 1 lakh can be deposited in an account at a time")
        else:
            self._balance=self._balance+amount
            return self._balance

    def withdraw_from_account(self,amount):
        if self._balance-amount<=10000:
            raise MinAmount("Min balance 10000 must be maintained while withdrawal")
        else:
            self._balance=self._balance-amount
            return self._balance


e1=User(101,"prati",4000)
print('''2 menu options
1. Deposit
2. Withdraw''')
num1=input("enter your choice: ")
if num1=="1":
    print(e1.deposit_to_account(57688))
