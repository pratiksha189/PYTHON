from BaseClass import Account

def DepositLimitExceededError(Exception):
    pass

def InvalidAmountError(Exception):
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