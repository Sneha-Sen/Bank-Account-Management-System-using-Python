import os

# A class to represent a bank account
class BankAccount:
    def __init__(self, acc_id, name, balance):
        self.acc_id = acc_id
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"₹{amount} deposited successfully.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"₹{amount} withdrawn successfully.")

    def display(self):
        print(f"Account ID: {self.acc_id}")
        print(f"Name: {self.name}")
        print(f"Balance: ₹{self.balance}")

# Global variable to store all accounts
accounts = {}
next_id = 1001

# Load accounts from file (if exists)
def load_accounts():
    global next_id
    if os.path.exists("accounts.txt"):
        with open("accounts.txt", "r") as file:
            for line in file:
                acc_id, name, balance = line.strip().split(",")
                accounts[int(acc_id)] = BankAccount(int(acc_id), name, float(balance))
            if accounts:
                next_id = max(accounts.keys()) + 1

# Save all accounts to file
def save_accounts():
    with open("accounts.txt", "w") as file:
        for acc in accounts.values():
            file.write(f"{acc.acc_id},{acc.name},{acc.balance}\n")

# Create new account
def create_account():
    global next_id
    name = input("Enter your name: ")
    try:
        amount = float(input("Enter initial deposit: "))
        acc = BankAccount(next_id, name, amount)
        accounts[next_id] = acc
        print(f"Account created! Your account ID is: {next_id}")
        next_id += 1
        save_accounts()
    except ValueError:
        print("Invalid amount. Try again.")

# Deposit money to an account
def deposit_money():
    try:
        acc_id = int(input("Enter your account ID: "))
        if acc_id in accounts:
            amount = float(input("Enter amount to deposit: "))
            accounts[acc_id].deposit(amount)
            save_accounts()
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Try again.")

# Withdraw money from an account
def withdraw_money():
    try:
        acc_id = int(input("Enter your account ID: "))
        if acc_id in accounts:
            amount = float(input("Enter amount to withdraw: "))
            accounts[acc_id].withdraw(amount)
            save_accounts()
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Try again.")

# View account details
def view_account():
    try:
        acc_id = int(input("Enter your account ID: "))
        if acc_id in accounts:
            print("\nAccount Details:")
            accounts[acc_id].display()
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid input. Try again.")

# MAIN PROGRAM
load_accounts()

while True:
    print("\n-- Welcome to Bank --")
    print("1. Create Account")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Account")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        create_account()
    elif choice == "2":
        deposit_money()
    elif choice == "3":
        withdraw_money()
    elif choice == "4":
        view_account()
    elif choice == "5":
        print("Thank you for banking with us!")
        break
    else:
        print("Invalid choice. Try again.")

