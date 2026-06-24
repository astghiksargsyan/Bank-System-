from models.bank_account import BankAccount
from models.savings_account import SavingsAccount

def change_interest_rate_function():
    rate_input = int(input("Enter the value of the interest rate input"))
    SavingsAccount.apply_interest(rate_input, rate_input)