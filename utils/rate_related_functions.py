from models.bank_account import BankAccount
from models.savings_account import SavingsAccount


def change_interest_rate_function():
    rate_input = float(input("Enter the new interest rate: "))
    SavingsAccount.change_interest_rate(rate_input)