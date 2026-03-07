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

class Account:
    def __init__(self,account_id,name,balance):
       self._account_id=account_id
       self._name=name
       self._balance=balance


