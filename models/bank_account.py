import uuid

class BankAccount:
    total_accounts = 0
    interest_rate =  0.05
    def __init__(self, owner, password, account_type, bank_name):
        self.id = str(uuid.uuid4())
        self.__owner = owner
        self.__balance = 0 
        self.password = password
        self.bank_name = bank_name
        self.account_type = account_type
        self.history = []
        BankAccount.total_accounts += 1 
    @staticmethod
    def get_valid_bank():
        bank_list = ["InecoBank", "AmeriaBank"]
        while True:
            ask_bank_input = input("Enter bank (AmeriaBank/InecoBank): ")
            if ask_bank_input in bank_list:
                return ask_bank_input
            else:
                print("Invalid bank name. Please choose AmeriaBank or InecoBank.")
    @classmethod
    def get_account_info(cls):
        """Collect user information from user input."""
        owner_input = input("Enter the owner name: ")
        password_input = input("Enter the password for the account: ")
        bank_name_input = BankAccount.get_valid_bank()
        account_type_input =  input("Choose the account type (Saving/checking): ")
        return cls(owner_input, password_input, account_type_input, bank_name_input)
    def create_single_account(self):
        """Create a dictionary representation of the account for JSON storage."""
        tmp = {}
        tmp["id"] = self.id
        tmp["owner"] = self.owner
        tmp["password"] = self.password
        tmp["balance"] = self.__balance
        tmp["bank_name"] = self.bank_name
        tmp["account_type"] = self.account_type
        tmp["history"] = self.history 
        return tmp
    @property
    def balance(self):
        return self.__balance
    @balance.setter
    def balance(self, value):
        """Blance setter"""
        if value < 0:
            print("The balance cannot be a negative value")
            self.__balance = 0  
        else:
            self.__balance = value
    @property
    def owner(self):
        return self.__owner
    def check_balance(self):
        """Returns the available balance"""
        return self.balance
    def deposit(self, amount):
        """Deposit function"""
        if amount <= 0:
            print("Deposit must be positive")
            return
        self.balance += amount
        self.history.append(f"Deposit: ${amount}")
    def withdraw(self, amount):
        """Withraw function """
        if amount <= 0:
            print("Withdraw must be positive")
            return
        if amount > self.balance:
            print("The balance is not enough")
        else:
            self.balance -= amount
        self.history.append(f"Withdrawal: ${amount}")
    @classmethod
    def change_interest_rate(cls, value):
        """Change interest rate for all accounts"""
        cls.interest_rate = value
    @classmethod
    def from_dict(cls, data):
        """Creates the object from json dictionary"""
        obj = cls(
                data.get("owner"),
                data.get("password"),
                data.get("account_type"),
                data.get("bank_name")
        )
        obj.id = data["id"]
        obj.balance = data["balance"]
        obj.history = data.get("history", [])
        return obj
    
    def __str__(self):
        """Return a readable string representation of the account owner.""" 
        return f"{self.owner} has ${self.balance} available balance. The history of transactions {self.history}"
    def __repr__(self):
        return f"BankAccount('{self.owner}', {self.balance})"

