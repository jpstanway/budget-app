class Category:
    ledger = []

    def __init__(self, category):
        self.category = category

    def deposit(self, amt, desc=''):
        self.ledger.append({"amount": amt, "description": desc})

    def withdraw(self, amt, desc=''):
        haveFunds = self.check_funds(amt)

        if (haveFunds):
            self.ledger.append({"amount": -abs(amt), "description": desc})
            return True

        return False

    def get_balance(self):
        balance = 0

        for transaction in self.ledger:
            balance += float(transaction['amount'])

        return balance

    def transfer(self, amt, category):
        return True

    def check_funds(self, amt):
        balance = self.get_balance()

        if (amt > balance):
            return False

        return True


def create_spend_chart(categories):
    return categories
