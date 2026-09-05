import random
import RandomFullNameGenerator as rfn

class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else:
            print("Insufficient funds")

    def get_balance(self):
        return self.balance

    def display_account_info(self):
        print(f"Account Number: {self.account_number}")
        print(f"Name: {self.name}")
        print(f"Balance: ${self.balance:,}")

accounts = []

for i in range(20):
    account = BankAccount(account_number=f"{i+1}", name=f"{rfn.generate_name()}", balance=random.randint(100, 1000000))
    accounts.append(account)

while True:
    print("1. Display all accounts")
    print("2. View an account")
    print("3. Deposit")
    print("4. Withdraw")
    print("5. Exit")

    user_input = input("Enter your choice: ")

    match user_input:
        case "1":
            for account in accounts:
                account.display_account_info()
                print()
        case "2":
            user_input_id = input("Enter account ID: ")
            print()
            for account in accounts:
                if account.account_number == user_input_id:
                    account.display_account_info()
                    print()
                    break
            else:
                print("Account not found")
        case "3":
            user_input_id = input("Enter account ID: ")
            print()
            for account in accounts:
                if account.account_number == user_input_id:
                    print("Account found:")
                    account.display_account_info()
                    print()
                    user_deposit_amount = input("How much to deposit?: ")
                    account.deposit(int(user_deposit_amount))
                    print (f"Money deposited. New balance: ${account.get_balance():,}")
                    break
        case "4":
            user_input_id = input("Enter account ID: ")
            print()
            for account in accounts:
                if account.account_number == user_input_id:
                    print("Account found:")
                    account.display_account_info()
                    print()
                    user_deposit_amount = input("How much to withdraw?: ")
                    account.withdraw(int(user_deposit_amount))
                    print (f"Money withdrawn. New balance: ${account.get_balance():,}")
                    break
        case "5":
            print("Exiting program.")
            break
        case _:
            print("Unknown command.")