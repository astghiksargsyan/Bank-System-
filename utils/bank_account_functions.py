from models.bank_account import BankAccount 
from utils.file_operations import load_data
from utils.file_operations import save_data
from utils.file_operations import update_data

def add_account():
    """Create a new account and save it to the JSON file."""
    account = BankAccount.get_account_info()
    save_data(account)
def login_function():
    login_input = input("Enter owner name: ")
    password_input = input("Enter password: ")
    accounts = load_data()
    Flag = True
    for account in accounts:
        if account["owner"] == login_input and account["password"] == password_input:
            print("Successfully logged in")
            Flag = False
            return BankAccount.from_dict(account) 
    if Flag:
        print("Wrong login information")
    

def view_balance():
    print("First login to make view balance")
    current_account = login_function()
    print(f"The current balance of {current_account.owner} is ${current_account.balance}")   
def deposit_function():
    print("First login to make deposit")
    current_account = login_function()
    deposit_input = input("Enter the ammount of deposit")
    current_account.deposit(int(deposit_input))
    update_data(current_account)
def withdraw_function():
    print("First login to make withdraw")
    current_account = login_function()
    withdraw_input = input("Enter the ammount of withdraw")
    current_account.withdraw(int(withdraw_input))
    update_data(current_account)
def view_accounts():
    accounts = load_data()
    print("Available accounts: ")
    for account in accounts:
        print(
            f"The owner: {account['owner']}\n"
            f"Account type: {account['account_type']}\n"
            f"Trancaction history {account['history']}"
        )

def change_account_type():
    print("First login to change account type")
    current_account = login_function()
    type_input = input("Enter the Account type (Saving or checking) : ")
    if type_input == "Saving" and current_account.account_type !=  "Saving":
            current_account.account_type = "Saving"
    elif type_input == "Checking" and current_account.account_type  !=  "Checking":
            current_account.account_type = "Checking"
    else: 
        print("Incorrect Value. Choose anothe value. ")
    update_data(current_account)

def transaction_between_accounts():
    accounts = load_data()
    print("First login to make transaction")
    current_account = login_function()
    reciver_account = input("Enter the username of the account you want to transfer money: ")
    amount =  float(input("Enter the amount: "))
    for account in accounts:
        if reciver_account == account["owner"]:
            receiver_account = BankAccount.from_dict(account)

    if current_account.balance < amount:
        print("The blance is not enought")
    else:
        current_account.withdraw(amount)
        receiver_account.deposit(amount)

        update_data(current_account)
        update_data(receiver_account)

        print("Transfer completed successfully")

def view_statistic():
    accounts = load_data()
    if not accounts:
        print("No accounts found.")
        return
    print(f"Currently, the number of accounts is: {len(accounts)}")
    total_sum = 0
    for account in accounts:
        total_sum += account["balance"]
    print(f"Total money in all accounts: {total_sum}")