from models.bank_account import BankAccount 
import json
ACCOUNT_FILE = "data/accounts.json"

def load_data():
    """Load the account list from the file"""
    try:
        with open(ACCOUNT_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []
def save_data(accounts, account): 
    accounts = load_data() 
    accounts.append(account.create_single_account()) 
    with open(ACCOUNT_FILE, "w", encoding="utf-8") as f: 
        json.dump(accounts, f, indent=4)
def update_data(updated_account):
    accounts = load_data()
    for i, acc in enumerate(accounts):
        if acc["id"] == updated_account.id:
            accounts[i] = updated_account.create_single_account()
            break
    with open(ACCOUNT_FILE, "w", encoding="utf-8") as f:
        json.dump(accounts, f, indent=4)