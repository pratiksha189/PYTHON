from BaseClass import Account
from ChildClass import SavingsAccount, CurrentAccount
from TransactionClass import Transaction

if __name__ == "__main__":
    transaction_list = []
    # user_input1 = SavingsAccount(101, "Ashish", 70000, "corporate")
    user_input1 = SavingsAccount(102, "Pratiksha", 90000, "personal")
    # user_input1 = CurrentAccount(103, "Pranita",96000)

    transaction = Transaction()

    while True:
        print("---------------------------------------")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Exit")
        print("---------------------------------------")
        choice = int(input("Enter choice: "))
        print("---------------------------------------")
        print(f'Your account type : {user_input1.acc_type}')
        try:
            if choice == 1:
                amount = int(input("Enter amount to deposit: "))
                balance = transaction.deposit_to_account(user_input1, amount)
                transaction_list.append(f"Deposit: {amount}")
                print("Deposit successful")
                print("Current Balance:", balance)


            elif choice == 2:
                amount = int(input("Enter amount to withdraw: "))
                balance = transaction.withdraw_from_account(user_input1, amount)
                transaction_list.append(f"Debited from {balance}: remaining amount = {amount}")
                print("Withdrawal successful")
                print("Current Balance:", balance)

            elif choice == 3:
                print("\nTransaction Statement")
                print("------------------------")
                for h in transaction_list:
                    print(h)
                print("\nFinal Balance:", balance)
                print("-----------------------------")
                break

            else:
                print("Invalid choice")
        except Exception as e:
            print("Error:", e)
