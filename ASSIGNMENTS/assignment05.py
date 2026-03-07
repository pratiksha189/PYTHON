# -----------------------------------------------------------------------
'''
Q.2 Create an Account class Heirarchy
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
Create user class with user interface that gives 2 menu options
1. Deposit
2. Withdraw
Both options will ask user to enter money to withdraw/deposit
Display a statement with each transaction and final balance after user exits from the menu
Identify possible Exceptions and implement them
'''
# ----------------------------------------------------------------
from abc import ABC, abstractmethod

def DepositLimitExceededError(Exception):
    pass

def InvalidAmountError(Exception):
    pass
# ----------------------------------------------------------------
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
# ----------------------------------------------------------------
class SavingsAccount(Account):
    def __init__(self, acc_id, name, balance, acc_type):
        self.acc_type = acc_type
        super().__init__(acc_id, name, balance)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit must be positive")
        if amount > 100000:
            raise DepositLimitExceededError("Max deposit is 1 lakh")
        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount")

        if self.acc_type == "corporate":
            if amount > self.balance:
                raise InvalidAmountError("Not enough balance")
            self.balance -= amount
            return self.balance

        else:  # personal account
            if self.balance - amount < 5000:
                raise InvalidAmountError("Minimum balance 5000 required")
            self.balance -= amount
            return self.balance
        # ---------------------------------------------------------------
class CurrentAccount(Account):
    def __init__(self, acc_id, name, balance):
        super().__init__(acc_id, name, balance)

    def deposit(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Deposit must be positive")

        if amount > 200000:
            raise DepositLimitExceededError("Maximum deposit is 2 lakh")

        self.balance += amount
        return self.balance

    def withdraw(self, amount):
        if amount <= 0:
            raise InvalidAmountError("Invalid withdrawal amount")

        if self.balance - amount < 10000:
            raise InvalidAmountError("Minimum balance 10000 required")

        self.balance -= amount
        return self.balance
# ----------------------------------------------------------------
class Transaction:
    def withdraw_from_account(self, account, amount):
        new_balance = account.withdraw(amount)
        return new_balance

    def deposit_to_account(self, account, amount):
        new_balance = account.deposit(amount)
        return new_balance
# ----------------------------------------------------------------
class UserApp:
    def start(self):
        acc = SavingsAccount(101, "Ashish", 70000, "corporate")
        history = []
        transaction = Transaction()

        while True:
            print("\n1. Deposit")
            print("2. Withdraw")
            print("3. Exit")
            choice = int(input("Enter choice: "))
            try:
                if choice == 1:
                    amount = int(input("Enter amount to deposit: "))
                    balance = transaction.deposit_to_account(acc, amount)
                    history.append(f"Deposit: {amount}")
                    print("Deposit successful")
                    print("Current Balance:", balance)


                elif choice == 2:
                    amount = int(input("Enter amount to withdraw: "))
                    balance = transaction.withdraw_from_account(acc, amount)
                    history.append(f"Withdraw: {amount}")
                    print("Withdrawal successful")
                    print("Current Balance:", balance)

                elif choice == 3:
                    print("\nTransaction Statement")
                    print("------------------------")
                    for h in history:
                        print(h)
                    print("\nFinal Balance:", acc.balance)
                    print("-----------------------------")
                    break

                else:
                    print("Invalid choice")
            except Exception as e:
                print("Error:", e)
# ----------------------------------------------------------------
app = UserApp()
app.start()
# ----------------------------------------------------------------

