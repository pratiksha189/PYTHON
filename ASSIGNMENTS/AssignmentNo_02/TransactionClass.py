from BaseClass import Account

# ----------------------------------------------------------------
class Transaction:
    @staticmethod
    def withdraw_from_account(account : Account, amount):
        new_balance = account.withdraw(amount)
        return new_balance

    @staticmethod
    def deposit_to_account(account : Account, amount):
        new_balance = account.deposit(amount)
        return new_balance
# ----------------------------------------------------------------