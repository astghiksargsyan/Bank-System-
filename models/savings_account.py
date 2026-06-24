from models.bank_account import BankAccount

class SavingsAccount(BankAccount):
    interest_rate =  0.05
    def apply_interest(self, interest_rate):
        interest = self.balance * self.interest_rate
        self.balance += interest
        self.history.append(f"Interest added: {interest}")
        print(f"Interest added: {interest}")
