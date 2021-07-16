class Category:
    ledger = []

    def __init__(self, category):
        self.category = category

    def deposit(self, amt, desc=''):
        self.ledger.append({"amount": amt, "description": desc})

    def withdraw(self, amt, desc=''):
        return True

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += int(transaction['amount'])

        return balance

    def transfer(self, amt, category):
        return True

    def check_funds(self, amt):
        return True


def create_spend_chart(categories):
    return categories
