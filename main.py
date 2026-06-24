from utils.bank_account_functions import add_account 
from utils.bank_account_functions import view_accounts
from utils.bank_account_functions import view_statistic
from utils.bank_account_functions import login_function
from utils.bank_account_functions import view_balance
from utils.bank_account_functions import deposit_function
from utils.bank_account_functions import withdraw_function
from utils.bank_account_functions import change_account_type
from utils.rate_related_functions import change_interest_rate_function
from models.bank_account import BankAccount
from models.savings_account import SavingsAccount
    
 
init_options = (
    ("1", "Create Account", add_account),
    ("2", "View All Accounts of bank", view_accounts),
    ("3", "Change Account Type", change_account_type),  
    ("4", "Login", login_function),
    ("5", "Change Interest Rate", change_interest_rate_function),
    ("6", "View Bank Statistics", view_statistic),
    ("7", "View Balance", view_balance),
    ("8", "Withdraw", withdraw_function),
    ("9", "Deposit", deposit_function) 
)

def main():
    print("Choose available option: ")
    print("#"*25)
    for num, name, __ in init_options:
        print(f"{num}: {name}")
    initial_input = input("Choose the option: ")
    Flag = True
    for num, name, funct in init_options:
        if initial_input == num or initial_input == name:
            funct()
            Flag = False
    if Flag:
        print("Not such an option, please check teh correct opration type")
main()